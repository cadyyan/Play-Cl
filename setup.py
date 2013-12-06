"""
Setup script for play-cl using setuptools
"""

from setuptools import setup, find_packages

setup(
	name			 = 'Play-CL',
	version			 = '0.0.0.0',
	description		 = 'Google Play commandline player.',
	author			 = 'Cadyyan',
	license			 = 'MIT',
	packages		 = find_packages(),
	install_requires = [
		'gmusicapi',
		'npyscreen',
	],
)

