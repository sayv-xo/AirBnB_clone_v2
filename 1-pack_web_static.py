#!/usr/bin/python3
""" Compress contents from a folder """

from datetime import datetime
from fabric.api import local
import os


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
