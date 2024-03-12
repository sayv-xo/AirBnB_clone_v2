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
    no_ext = filename.split(".")[0]
    full_path = "/data/web_static/releases/" + no_ext
    try:
        # upload archive file to tmp dir of server
        put(archive_path, '/tmp/')
        # create directories
        run("mkdir -p /data/web_static/releases/{}".format(no_ext))
        # uncompress archive file
        run("tar -xzf /tmp/{} -C {}/".format(filename, full_path))
        run("rm /tmp/{}".format(filename))
        run("mv {}/web_static/* {}/".format(full_path))
        run("rm -rf {}/web_static".format(full_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(full_path))
        print("New version deployed!")
        return True
    except Exception:
        return False
