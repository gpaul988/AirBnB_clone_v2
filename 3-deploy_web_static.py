#!/usr/bin/python3
""" Graham S. Paul (3-deploy_web_static.py) - Share archive to web servers, using function do_deploy """
from fabric.api import env, put, run, local
import os.path
from time import strftime
env.hosts = ['web1.gpaul.info', 'web2.gpaul.info']


def do_pack():
    '''Generate required files'''
    timenow = strftime('%Y%M%d%H%M%S')
    try:
        local('mkdir -p versions')
        filename = 'versions/web_static_{}.tgz'.format(timenow)
        local('tar -czvf {} web_static/'.format(filename))
        return filename
    except Exception:
        return None


def do_deploy(archive_path):
    '''Upload achive to web servers'''
    if not os.path.isfile(archive_path):
        return False
    try:
        filename = archive_path.split('/')[-1]
        no_ext = filename.split('.')[0]
