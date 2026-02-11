# -*- coding: utf-8 -*-
'''
dummy: a bare-bone Python library to debug https://stackoverflow.com/questions/79887269/

Copyright (c) 2026 F.P.A. Vogt; frederic.vogt@alumni.anu.edu.au

Distributed under the terms of the GNU General Public License v3.0 or later.

SPDX-License-identifier: GPL-3.0-or-later
'''

from setuptools import setup, find_packages # Always prefer setuptools over distutils

setup(name='dummy',
      version='0.0.1',
      author='fpavogt',
      author_email='frederic.vogt@alumni.anu.edu.au',
      # Include all packages under src
      packages=find_packages(where="src"),
      # Tell setuptools packages are under src
      package_dir={"": "src"},

      url='https://github.com/fpavogt/dummy',
      project_urls={
        'Source': 'https://github.com/fpavogt/dummy',
        'Changelog': 'https://github.com/fpavogt/dummy#changelog',
        'Issues': 'https://github.com/fpavogt/dummy/issues'
      },
      license='GNU General Public License v3 or later (GPLv3+)',
      description='DUmmy Python module',
      python_requires='>=3',
      install_requires=[],
      entry_points={},
      include_package_data=False,
      )
