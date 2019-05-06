[![license](https://img.shields.io/pypi/l/refuse.svg?style=flat-square "Internet Systems Consortium License")](https://github.com/pleiszenburg/refuse/blob/master/LICENSE) [![status](https://img.shields.io/pypi/status/refuse.svg?style=flat-square "Project Development Status")](https://github.com/pleiszenburg/refuse/milestone/3) [![pypi_version](https://img.shields.io/pypi/v/refuse.svg?style=flat-square "Project Development Status")](https://pypi.python.org/pypi/refuse) [![pypi_versions](https://img.shields.io/pypi/pyversions/refuse.svg?style=flat-square "Available on PyPi - the Python Package Index")](https://pypi.python.org/pypi/refuse)

![refuse](http://www.pleiszenburg.de/refuse_logo.png)

## Synopsis

`refuse` is a Python module implemented using [`ctypes`](https://docs.python.org/3/library/ctypes.html) that provides a simple cross-platform interface to:

- [libfuse](https://github.com/libfuse/libfuse)
- [FUSE for macOS](https://osxfuse.github.io/)
- [WinFsp](https://github.com/billziss-gh/winfsp)

`refuse` originated as a fork of [`fusepy`](https://github.com/fusepy/fusepy). This fork will break with its origins in (at least) the following aspects:

* Dropping Python 2 support
* Dropping the monolithic single-file-design
* Adding ``libfuse3`` support
* Marking ``libfuse2`` support as deprecated
* A test suite

**If you have a pending pull request against `fusepy` that you would like to see included into `refuse` please open an issue here.**

## Project status

THIS PROJECT HAS **ALPHA** STATUS. The high level API has been tested through [`LoggedFS-python`](https://github.com/pleiszenburg/loggedfs-python) with [`pjdfstest`](https://github.com/pjd/pjdfstest/) and [`fsx`](https://github.com/linux-test-project/ltp/blob/master/testcases/kernel/fs/fsx-linux/fsx-linux.c), but not in all possible modes of operation. The low level API is completely untested at this point.

## Installation

`refuse` requires `libfuse` 2.8 or 2.9 (highly recommended), `FUSE for macOS` or `WinFsp`. It (theoretically) runs on:

* Linux (i386, x86_64, PPC, arm64, MIPS)
* Mac OS X (Intel, PowerPC)
* FreeBSD (i386, amd64)
* OpenBSD (all architectures, high level bindings only)
* Windows (?)
* Windows/Cygwin (?)

## Porting a project from `fusepy` to `refuse`

[See documentation](https://github.com/pleiszenburg/refuse/blob/master/docs/porting.md).

## Miscellaneous

- [Authors](https://github.com/pleiszenburg/refuse/blob/master/AUTHORS.md) (credit where credit is due)
- [Change log](https://github.com/pleiszenburg/refuse/blob/master/CHANGES.md) (release history)
- [Contributing](https://github.com/pleiszenburg/refuse/blob/master/CONTRIBUTING.md) (**Contributions are highly welcomed!**)
- [Documentation](https://github.com/pleiszenburg/refuse/tree/master/docs) (mostly notes at this point)
- [License](https://github.com/pleiszenburg/refuse/blob/master/LICENSE) (**ISCL**)
