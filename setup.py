#!/usr/bin/env python

from setuptools import setup

setup(
  name='HyperglassBird',
  version='1.0',
  packages=['hyperglass_bird'],
  entry_points = {
    'console_scripts': ['hyperglass-bird=hyperglass_bird.hyperglass_bird']
  },
  install_requires = [
    'toml',
    'click',
    'flask',
    'logzero',
    'passlib',
    'waitress',
  ],
)
