#!/usr/bin/env python

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
