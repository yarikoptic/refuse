[![license](https://img.shields.io/pypi/l/refuse.svg?style=flat-square "Internet Systems Consortium License")](https://github.com/pleiszenburg/refuse/blob/master/LICENSE) [![status](https://img.shields.io/pypi/status/refuse.svg?style=flat-square "Project Development Status")](https://github.com/pleiszenburg/refuse/milestone/3) [![pypi_version](https://img.shields.io/pypi/v/refuse.svg?style=flat-square "Project Development Status")](https://pypi.python.org/pypi/refuse) [![pypi_versions](https://img.shields.io/pypi/pyversions/refuse.svg?style=flat-square "Available on PyPi - the Python Package Index")](https://pypi.python.org/pypi/refuse)

![refuse](http://www.pleiszenburg.de/refuse_logo.png)

## Synopsis

`refuse` is a Python module implemented using [`ctypes`](https://docs.python.org/3/library/ctypes.html) that provides a simple cross-platform interface to:

- [libfuse](https://github.com/libfuse/libfuse)
- [FUSE for macOS](https://osxfuse.github.io/)
- [WinFsp](https://github.com/billziss-gh/winfsp)

`refuse` originated as a fork of [`fusepy`](https://github.com/fusepy/fusepy). This fork will break with its origins in (at least) the following aspects:

- [x] Dropping Python 2 support
- [ ] Dropping the monolithic single-file-design
- [ ] Adding ``libfuse3`` support
- [ ] Marking ``libfuse2`` support as deprecated
- [ ] A test suite

**If you have a pending pull request against `fusepy` that you would like to see included into `refuse` please open an issue here.**

**If you want to contribute to `refuse`, please have a look at the [contributing guidelines](https://github.com/pleiszenburg/refuse/blob/develop/CONTRIBUTING.md).**

## Project status

THIS PROJECT HAS **ALPHA** STATUS.

The high level API has been tested through [`LoggedFS-python`](https://github.com/pleiszenburg/loggedfs-python) with [`pjdfstest`](https://github.com/pjd/pjdfstest/) and [`fsx`](https://github.com/linux-test-project/ltp/blob/master/testcases/kernel/fs/fsx-linux/fsx-linux.c) on x86_64 Linux only, but not in all possible modes of operation. The low level API is completely untested at this point.

## Installation

`refuse` requires `libfuse` 2.8 or 2.9 (highly recommended), `FUSE for macOS` or `WinFsp`. The [`master` branch](https://github.com/pleiszenburg/refuse/tree/master) of its git repository is always kept at the latest *preview release*. It should be "sort of stable" (still ALPHA). Development happens in the [`develop` branch](https://github.com/pleiszenburg/refuse/tree/develop).

You can install the *preview releases* from PyPI:

```bash
pip install refuse
```

You can alternatively also install the current `HEAD`, most likely very unstable:

```bash
pip install git+https://github.com/pleiszenburgrefuse.git@develop
```

`refuse` (theoretically) runs on:

<table>
  <tr>
    <th>OS</th><th colspan="2">API</th><th colspan="6">arch</th>
  </tr>
  <tr>
    <th></th><th>level</th><th>version</th>
    <th>i386</th><th>x86_64</th><th>PPC</th><th>PPC64</th><th>arm64</th><th>MIPS</th>
  </tr>
  <tr>
    <td rowspan="4">Linux</td><td rowspan="2">high</td><td>2</td>
    <td>yes</td><td>yes</td><td>yes</td><td>yes</td><td>yes</td><td>yes</td>
  </tr>
  <tr>
    <td>3</td>
    <td>no</td><td>no</td><td>no</td><td>no</td><td>no</td><td>no</td>
  </tr>
  <tr>
    <td rowspan="2">low</td><td>2</td>
    <td>yes</td><td>yes</td><td>yes</td><td>yes</td><td>yes</td><td>yes</td>
  </tr>
  <tr>
    <td>3</td>
    <td>no</td><td>no</td><td>no</td><td>no</td><td>no</td><td>no</td>
  </tr>
  <tr>
    <td rowspan="4">Mac OS X</td><td rowspan="2">high</td><td>2</td>
    <td>yes</td><td>yes</td><td>yes</td><td>yes</td><td></td><td></td>
  </tr>
  <tr>
    <td>3</td>
    <td>no</td><td>no</td><td>no</td><td>no</td><td></td><td></td>
  </tr>
  <tr>
    <td rowspan="2">low</td><td>2</td>
    <td>yes</td><td>yes</td><td>yes</td><td>yes</td><td></td><td></td>
  </tr>
  <tr>
    <td>3</td>
    <td>no</td><td>no</td><td>no</td><td>no</td><td></td><td></td>
  </tr>
  <tr>
    <td rowspan="4">FreeBSD</td><td rowspan="2">high</td><td>2</td>
    <td>yes</td><td>yes</td><td>no</td><td>no</td><td>no</td><td>no</td>
  </tr>
  <tr>
    <td>3</td>
    <td>no</td><td>no</td><td>no</td><td>no</td><td>no</td><td>no</td>
  </tr>
  <tr>
    <td rowspan="2">low</td><td>2</td>
    <td>yes</td><td>yes</td><td>no</td><td>no</td><td>no</td><td>no</td>
  </tr>
  <tr>
    <td>3</td>
    <td>no</td><td>no</td><td>no</td><td>no</td><td>no</td><td>no</td>
  </tr>
  <tr>
    <td rowspan="4">OpenBSD</td><td rowspan="2">high</td><td>2</td>
    <td>yes</td><td>yes</td><td>yes</td><td>yes</td><td>yes</td><td>yes</td>
  </tr>
  <tr>
    <td>3</td>
    <td>no</td><td>no</td><td>no</td><td>no</td><td>no</td><td>no</td>
  </tr>
  <tr>
    <td rowspan="2">low</td><td>2</td>
    <td>no</td><td>no</td><td>no</td><td>no</td><td>no</td><td>no</td>
  </tr>
  <tr>
    <td>3</td>
    <td>no</td><td>no</td><td>no</td><td>no</td><td>no</td><td>no</td>
  </tr>
  <tr>
    <td rowspan="4">Windows</td><td rowspan="2">high</td><td>2</td>
    <td>yes</td><td>yes</td><td></td><td></td><td>no</td><td></td>
  </tr>
  <tr>
    <td>3</td>
    <td>no</td><td>no</td><td></td><td></td><td>no</td><td></td>
  </tr>
  <tr>
    <td rowspan="2">low</td><td>2</td>
    <td>no</td><td>no</td><td></td><td></td><td>no</td><td></td>
  </tr>
  <tr>
    <td>3</td>
    <td>no</td><td>no</td><td></td><td></td><td>no</td><td></td>
  </tr>
  <tr>
    <td rowspan="4">Windows/Cygwin</td><td rowspan="2">high</td><td>2</td>
    <td>yes</td><td>yes</td><td></td><td></td><td>no</td><td></td>
  </tr>
  <tr>
    <td>3</td>
    <td>no</td><td>no</td><td></td><td></td><td>no</td><td></td>
  </tr>
  <tr>
    <td rowspan="2">low</td><td>2</td>
    <td>no</td><td>no</td><td></td><td></td><td>no</td><td></td>
  </tr>
  <tr>
    <td>3</td>
    <td>no</td><td>no</td><td></td><td></td><td>no</td><td></td>
  </tr>
</table>

## Porting a project from `fusepy` to `refuse`

[See documentation](https://github.com/pleiszenburg/refuse/blob/master/docs/porting.md).

## Miscellaneous

- [Authors](https://github.com/pleiszenburg/refuse/blob/master/AUTHORS.md) (credit where credit is due)
- [Change log (current)](https://github.com/pleiszenburg/refuse/blob/develop/CHANGES.md) (changes in development branch since last release)
- [Change log (past)](https://github.com/pleiszenburg/refuse/blob/master/CHANGES.md) (release history)
- [Contributing](https://github.com/pleiszenburg/refuse/blob/develop/CONTRIBUTING.md) (**Contributions are highly welcomed!**)
- [Documentation](https://github.com/pleiszenburg/refuse/tree/master/docs) (mostly notes at this point)
- [License](https://github.com/pleiszenburg/refuse/blob/master/LICENSE) (**ISCL**)
