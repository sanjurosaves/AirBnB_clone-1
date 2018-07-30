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
do_pack = __import__('1-pack_web_static')
do_deploy = __import__('2-do_deploy_web_static')
env.hosts = ['35.237.92.195', '35.237.197.1']


def deploy():
    paff = do_pack.do_pack()
    try:
        return do_deploy.do_deploy(paff)
    except:
        return False
