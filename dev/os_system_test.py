# PyTest
import sys
import pytest
import logging as log

import os
def test_is_windows():
    system_name = os.name
    # log.warning(system_name)
    assert system_name == 'nt'

def test_is_ubuntu():
    system_name = os.name
    # log.warning(system_name)
    assert system_name == 'posix'

if __name__ == '__main__':
    pytest.main(sys.argv)
