#!/usr/bin/python3
""" Compress contents from a folder """

from datetime import datetime
from fabric.api import local
import os

env.hosts = ['100.25.12.4', '52.91.127.130']


def do_pack():
    """ generate tgz archive """
    # check if versions folder exists or create it
    if not os.path.exists("versions"):
        local("mkdir versions")
    date = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    # create archive
    if local(f"tar -czvf {filename} web_static").failed is True:
        return None
    return filename


def do_deploy(archive_path):
    """ distribute archive to server """
    if os.path.exists(archive_path) is False:
        return False
    filename = archive_path.split("/")[-1]
    name = filename.split(".")[0]
    try:
        put(archive_path, '/tmp/')
        run("mkdir -p /data/web_static/releases/{}/".format(name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(filename, name))
        run("rm /tmp/{}".format(filename))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static".
            format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
            format(name))
        print("New version deployed!")
    except Exception:
        return False


def deploy():
    """pack web_static content and deploy it to web servers
    """
    archive = do_pack()
    if archive:
        return do_deploy(archive)
    return False
