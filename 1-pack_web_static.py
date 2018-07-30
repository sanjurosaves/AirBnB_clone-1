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
