# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in loan_appraiser/__init__.py
from loan_appraiser import __version__ as version

setup(
	name='loan_appraiser',
	version=version,
	description='Credit Scoring App',
	author='reworq',
	author_email='rsalimabdul@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
