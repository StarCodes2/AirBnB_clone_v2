#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents of the
web_static directory and deploy it to two servers. """
from os.path import isfile
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["18.214.89.20", "52.203.53.113"]


def do_deploy(archive_path):
    """ deploys the content of an archive to two servers. """
    if isfile(archive_path) is False:
        return False
    file_name = archive_path.split("/")[-1]
    name = file_name.split(".")[0]
    tmp = "/tmp/{}".format(file_name)

    if put(archive_path, tmp).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf {} -C /data/web_static/releases/{}/".
           format(tmp, name)).failed is True:
        return False
    if run("rm {}".format(tmp)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{} /data/web_static/current".
           format(name)).failed is True:
        return False

    return True
