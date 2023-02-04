import pathlib
import unittest
from pathlib import Path


class MyTestCase(unittest.TestCase):
    def test_something(self):
        ## __file__
        print(Path(__file__))
        print(Path(__file__).parent)
        print(Path(__file__).joinpath('..', '..', 'sqlite').resolve())


if __name__ == '__main__':
    unittest.main()


