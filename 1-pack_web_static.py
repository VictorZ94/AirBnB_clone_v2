#!/usr/bin/python3
from fabric.api import *
from datetime import datetime


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
