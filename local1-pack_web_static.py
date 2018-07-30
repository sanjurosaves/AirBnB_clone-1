#!/usr/bin/python3
from fabric.api import local
from fabric.api import get
from fabric.api import put
from fabric.api import reboot
from fabric.api import run
from fabric.api import sudo
from fabric.context_managers import cd
from fabric.api import env
import time

def do_pack():
    """ generates a .tgz archive from the contentes of web_static folder """
    local("mkdir -p versions; dt=$(date \"+%Y%m%d%H%M%S\"); \
    tar -cvzf versions/web_static_$dt.tgz /data/web_static/")
