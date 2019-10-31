# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in conference/__init__.py
from conference import __version__ as version

setup(
	name='conference',
	version=version,
	description='Conference & Ticketing Management',
	author='Frappe Technologies',
	author_email='developers@frappe.io',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
