#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
  name='pex-example',
  version='0.0.1',
  description="",
  author='Stephen Holsapple',
  author_email='sholsapp@gmail.com',
  url='https://github.com/sholsapp/pex-example',
  license='Apache License, Version 2.0',
  packages=find_packages(),
  install_requires=[
    'pex',
    'wheel',
  ],
  tests_require=[],
  entry_points={
    'console_scripts': [
      'pex-example = pexexample:main',
    ],
  },
)
