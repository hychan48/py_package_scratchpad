# PyTest
import sys
import pytest
import logging as log

import package_demo as pkg

def test_name():
    log.warning("hi")



if __name__ == '__main__':
    pytest.main(sys.argv)
