# How to contribute to *refuse*

Thank you for considering contributing to *refuse*!
**Contributions are highly welcomed!**

## Branching model

Development happens in the `develop` branch. Please issue pull requests against `develop`. The `master` branch is supposed to be kept at the least, more or less stable *preview release*.

## Language level & interpreters

This project targets Python 3 exclusively. Python 3.4 support is optional and can be dropped if required. Python 3.5 and later are mandatory as Python 3.5 is still widely used and supported. The primary target so far is CPython, although PyPy support is highly welcome.

## Operating system support

*refuse* is meant to be as generic as possible. Support for new operating systems and/or new platforms is always welcome. Have a look at the current support matrix in [README.md](https://github.com/pleiszenburg/refuse/blob/develop/README.md).

## General workflow

If you are planning on working on a "larger" issue or feature, please add yourself to the corresponding issue on GitHub or create a new one there - before you start working. This helps to reduce duplicate effort and allows to coordinate developers.

Everything is supposed to be tested. However, right now, *refuse* does not have a single test on its own. It can merely be tested through filesystems relying on it. This is currently done based on [LoggedFS-python](https://github.com/pleiszenburg/loggedfs-python) for x86_64 Linux. **The main objective therefore is to add a testing infrastructure.** New features are welcome, too, but tests come first. Tests based on Qemu are the likely way to go because Qemu can emulate all kinds of architectures on a single machine. Anything else that helps testing *refuse* is also highly welcome. Static code analysis comes to mind, for instance.
