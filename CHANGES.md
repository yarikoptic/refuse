# Changes

## 0.0.1 (2019-XX-XX)

The following changes were made based on state of `fusepy` as of 2019-05-04.

- FEATURE: OpenBSD support for high level API from [pull request 125 against `fusepy`](https://github.com/fusepy/fusepy/pull/125) was merged.
- FEATURE: Added support for `UTIME_OMIT` and `UTIME_NOW` to high level API. Enable it by adding an `flag_utime_omit_ok` property to your `refuse.high.Operations` sub-class and set it to `1` (integer).
- New Python project structure: [`src` folder](https://blog.ionelmc.ro/2014/05/25/python-packaging/), just a single top-level module named `refuse`
- Modernized `setup.py`, dropping support for Python 2 and `setuptools` < 30.0
- Examples declared legacy
