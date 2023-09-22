#!/usr/bin/python3
# Graham S. Paul (1-pack_web_static.py)
'''Script to create .tgz file from the inputs of webstatic
usage: fab -f 1-pack_web_static.py do_pack
'''
from fabric.api import local
from time import strftime


def do_pack():
    '''Create required files'''
    timenow = strftime('%Y%M%d%H%M%S')
    try:
        local('mkdir -p versions')
        filename = 'versions/web_static_{}.tgz'.format(timenow)
        local('tar -czvf {} web_static/'.format(filename))
        return filename
    except Exception:
        return None
