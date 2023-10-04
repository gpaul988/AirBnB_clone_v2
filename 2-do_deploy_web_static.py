#!/usr/bin/python3
# Graham S. Paul (2-do_deploy_web_static.py)
from fabric.contrib import files
from fabric.api import env, put, run
import os

env.hosts = ['54.82.216.202', '18.234.106.116']


def do_deploy(archive_path):
    """Function for deploy"""
    if not os.path.exists(archive_path):
        return False

    data_path = '/data/web_static/releases/'
    tmp = archive_path.split('.')[0]
    name = tmp.split('/')[1]
    dest = data_path + name

    try:
        put(archive_path, '/tmp')
        run('sudo mkdir -p {}'.format(dest))
        run('sudo tar -xzf /tmp/{}.tgz -C {}'.format(name, dest))
        run('sudo rm -f /tmp/{}.tgz'.format(name))
        run('sudo mv {}/web_static/* {}/'.format(dest, dest))
        run('sudo rm -rf {}/web_static'.format(dest))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(dest))
        return True
    except:
        return False
