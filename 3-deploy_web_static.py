#!/usr/bin/python3
""" Graham S. Paul (3-deploy_web_static.py) - Share archive to web servers, using function do_deploy """
from fabric.contrib import files
from fabric.api import env, put, run, local
import time
import os

env.hosts = ['54.82.216.202', '18.234.106.116']


def do_pack():
    """Gerenate tgz."""
    timestamp = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{:s}.tgz web_static/".
              format(timestamp))
        return ("versions/web_static_{:s}.tgz".format(timestamp))
    except:
        return None


def do_deploy(archive_path):
    """Function for deploy."""
    if not os.path.exists(archive_path):
        return False

    data_path = '/data/web_static/releases/'
    tmp = archive_path.split('.')[0]
    name = tmp.split('/')[1]
    dest = data_path + name
