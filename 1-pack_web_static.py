#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents of the
web_static directory. """
from datetime import datetime
from fabric.api import local


def do_pack():
	""" Creates a tar archive of the directory web_static. """
	if local("mkdir -p versions").failed is True:
		return None

	d = datetime.utcnow()
	arch = "versions/web_static_{}{}{}{}{}{}.tgz".format(d.year, d.month,
							     d.day, d.hour,
							     d.minute,
							     d.second)
	if local("tar -cvf {} web_static".format(arch)).failed is True:
		return None
	return arch
