import ctypes
from ..low import FUSELL, LibFUSE, fuse_args

import pytest


@pytest.fixture
def fusell(tmp_path):
    yield FUSELL(str(tmp_path))


def test_LibFUSE_mount_unmount(tmp_path):
    lib = LibFUSE()
    args = ['fuse']
    # worth moving into helper to be reused here
    argv = fuse_args(len(args), (ctypes.c_char_p * len(args))(*[arg.encode() for arg in args]), 0)
    chan = lib.fuse_mount(str(tmp_path).encode(), argv)
    lib.fuse_unmount(str(tmp_path).encode(), chan)


#
# likely fusell needs its own thread
#
#def test_nothing_much(fusell):
#    assert str(fusell)
#    assert repr(fusell)
