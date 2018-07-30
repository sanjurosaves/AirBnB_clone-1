#!/usr/bin/python3
from fabric.api import local
from fabric.api import get
from fabric.api import put
from fabric.api import reboot
from fabric.api import run
from fabric.api import sudo
from fabric.context_managers import cd
from fabric.api import env
from datetime import datetime
import os

env.hosts = ['35.237.92.195', '35.237.197.1']


def do_pack():
    """ generates a .tgz archive from the contentes of web_static folder """
    try:
        dt = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions; tar -P -cvzf versions/web_static_{}.tgz "
              "/data/web_static/".format(dt))
        ap = "versions/web_static_{}.tgz".format(dt)
        return ap
    except:
        return None


def do_deploy(archive_path):
    if os.path.esists(archive_path) is False:
        return False
    try:
        # upload archive (put) to tmp dir of webserver
        put(archive_path, '/tmp/')
        # uncompress
        archive_name = archive_path[9:-4]
        run('sudo mkdir -p /data/web_static/releases/{}'.format(archive_name))
        run('sudo tar -xzf /tmp/{}.tgz -C '
            '/data/web_static/releases/{}'
            .format(archive_name, archive_name))
        # delete archive
        run('rm /tmp/{}.tgz'.format(archive_name))
        run('sudo mv -f /data/web_static/releases/{}/web_static/* '
            '/data/web_static/releases/{}/'.format(archive_name,
                                                   archive_name))
        run('sudo rm -rf /data/web_static/releases/{}/web_static'
            .format(archive_name))
        # delete symbolic link
        run('sudo rm -rf /data/web_static/current')
        # create new symbolic link
        run('sudo ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(archive_name))
        print("New version deployed!")
        return True
    except:
        return False
