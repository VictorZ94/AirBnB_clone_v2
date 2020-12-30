#!/usr/bin/python3
""" Write a Fabric script """
from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ['35.237.76.6', '35.229.51.65']


def do_pack():
    """[summary]
    Returns:
        [type]: [description]
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(name))
        return name
    except:
        return None


def do_deploy(archive_path):
    """[summary]"""
    if exists(archive_path):
        file_path = archive_path.split("/")[1]
        serv_path = "/data/web_static/releases/{}".format(
            file_path.replace(".tgz", ""))
        put('{}'.format(archive_path), '/tmp/')
        run('mkdir -p {}'.format(serv_path))
        run('tar -xzf /tmp/{} -C {}/'.format(
            file_path,
            serv_path))
        run('rm /tmp/{}'.format(file_path))
        run('mv -f {}/web_static/* {}/'.format(serv_path, serv_path))
        run('rm -rf {}/web_static'.format(
            serv_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(
            serv_path))
        return True
    else:
        return False
