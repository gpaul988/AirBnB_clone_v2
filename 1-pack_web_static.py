#!/usr/bin/python3
# Graham S. Paul (1-pack_web_static.py)
from fabric.api import local
from time import strftime
from datetime import date


def do_pack():
    """ Script to create archive the contents of web_static folder"""

    filename = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(filename))

        return "versions/web_static_{}.tgz".format(filename)

    except Exception as e:
        return None
