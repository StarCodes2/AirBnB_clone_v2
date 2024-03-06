#!/usr/bin/python3
""" Deletes out-of-date archives, using the function do_clean. """
from os import listdir
from fabric.api import env, lcd, local, cd, run

env.hosts = ["54.88.33.51", "100.26.50.21"]


def do_clean(number=0):
    """Deletes out-of-date archives
    Args:
        number(int): Number of archives that won't be deleted
    """
    if int(number) == 0:
        number = 1
    else:
        number = int(number)

    archives = sorted(listdir("versions"))
    for i in range(number):
        archives.pop()

    with lcd("versions"):
        for archive in archives:
            local("rm ./{}".format(archive))

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        for i in range(number):
            archives.pop()
        for archive in archives:
            run("rm -rf ./{}".format(archive))
