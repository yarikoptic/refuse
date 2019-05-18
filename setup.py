# -*- coding: utf-8 -*-

"""

REFUSE
Simple cross-plattform ctypes bindings for libfuse / FUSE for macOS / WinFsp
https://github.com/pleiszenburg/refuse

    setup.py: Used for package distribution

    Copyright (C) 2008-2019 refuse contributors

<LICENSE_BLOCK>
The contents of this file are subject to the Internet Systems Consortium (ISC)
license ("ISC license" or "License"). You may not use this file except in
compliance with the License. You may obtain a copy of the License at
https://opensource.org/licenses/ISC
https://github.com/pleiszenburg/refuse/blob/master/LICENSE

Software distributed under the License is distributed on an "AS IS" basis,
WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for the
specific language governing rights and limitations under the License.
</LICENSE_BLOCK>

"""


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# IMPORT
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import os
from setuptools import find_packages, setup


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SETUP
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# BUMP VERSION HERE!
_version_ = '0.0.3'

# List all versions of Python which are supported
confirmed_python_versions = [
    ('Programming Language :: Python :: %s' % x)
    for x in '3.4 3.5 3.6 3.7'.split(' ')
    ]

# Fetch readme file
with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r') as f:
    long_description = f.read()

# Development dependencies
development_deps_list = [
    'coverage',
    'pytest',
    'python-language-server',
    'setuptools',
    'Sphinx',
    'sphinx_rtd_theme',
    'twine',
    'wheel'
    ]


setup(
    name = 'refuse',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    version = _version_,
    description = 'Simple cross-plattform ctypes bindings for libfuse / FUSE for macOS / WinFsp',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author = 'Sebastian M. Ernst',
    author_email = 'ernst@pleiszenburg.de',
    url = 'https://github.com/pleiszenburg/refuse',
    download_url = 'https://github.com/pleiszenburg/refuse/archive/v%s.tar.gz' % _version_,
    license = 'ISC',
    keywords = ['fuse', 'libfuse'],
    include_package_data = True,
    install_requires = [],
    extras_require = {'dev': development_deps_list},
    zip_safe = False,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: BSD',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3',
		] + confirmed_python_versions + [
        'Topic :: System :: Filesystems',
        ]
    )
