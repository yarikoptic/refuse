# refuse

## Synopsis

`refuse` is a Python module that provides a simple interface to [`libfuse`](https://github.com/libfuse/libfuse) and [FUSE for macOS](https://osxfuse.github.io/). It is implemented using [`ctypes`](https://docs.python.org/3/library/ctypes.html). It originated as a fork of [`fusepy`](https://github.com/fusepy/fusepy).

This fork will break with its origins (at least) in the following aspects:

* Dropping Python 2 support
* Dropping the monolithic single-file-design
* Adding ``libfuse3`` support
* Marking ``libfuse2`` support as deprecated
* A test suite

Longer term goals might include:

* Adding Windows support, as far as possible, based on the excellent work of billziss-gh, see [here](https://github.com/billziss-gh/fusepy) and [here](https://github.com/billziss-gh/winfsp)
* Adding OpenBSD support, as far as possible, based on the excellent work of rianhunter, see [here](https://github.com/rianhunter/fusepyng)

**If you have a pending pull request against `fusepy` that you would like to see included into `refuse` please open an issue here.**

## Project status

This project has **ALPHA** status. IT IS CURRENTLY UNTESTED AND CAN NOT BE INSTALLED.

## Installation

`refuse` requires `libfuse` 2.6 or later (2.9 is highly recommended) and theoretically runs on:

* Linux (i386, x86_64, PPC, arm64, MIPS)
* Mac OS X (Intel, PowerPC)
* FreeBSD (i386, amd64)
* Windows (?)
