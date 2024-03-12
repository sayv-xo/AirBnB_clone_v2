#!/usr/bin/python3
""" distribute archive to webserver """
import os
from fabric.api import put, run, env

env.hosts = ['100.25.12.4', '52.91.127.130']


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
