# import unittest
import pytest
from stringcolor import *
import sys

# https://stackoverflow.com/questions/284043/outputting-data-from-unit-test-in-python

# logging.basicConfig(stream=sys.stderr)

class TestCase:

    def test_something(self):
        import logging
        print('')
        print(cs("here we go", "orchid"))
        print(cs("here we go", "blue"))
        print(cs("here we go", "blue"))

        # logging.basicConfig(stream=sys.stdout)
        # logging.getLogger("TestCase.test_something").setLevel(logging.DEBUG)

        # log = logging.getLogger("TestCase.test_something")
        # print('start')
        # log.debug('before class')
        # log.debug('hi')
        # log = logging.getLogger(__name__)
        # log.error('hi')
        logging.error('hi')
        # interesting behavior for unittest...
        assert(1==1)


# if __name__ == '__main__':
#     unittest.main()
