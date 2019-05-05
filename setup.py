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

from setuptools import find_packages, setup

_version_ = '0.0.1' # BUMP VERSION HERE!

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name = 'refuse',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    version = _version_,
    description = 'Simple ctypes bindings for libfuse / FUSE',
    long_description = long_description,
    author = 'Sebastian M. Ernst',
    author_email = 'ernst@pleiszenburg.de',
    url = 'https://github.com/pleiszenburg/refuse',
    license = 'ISC',
    keywords = ['fuse', 'libfuse'],
    include_package_data = True,
    install_requires = [],
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
        'Programming Language :: Python :: 3',
        'Topic :: System :: Filesystems',
        ]
    )
