import os
import pathlib
import unittest
from pathlib import Path


# PyCharm is autodetect

# interesting... test.py doesnt work
# test_?
class MyTestCase(unittest.TestCase):
    def test_something(self):
        ## __file__
        print(Path(__file__))
        print(Path(__file__).parent)
        a = Path(__file__).joinpath('..', '..', 'sqlite').resolve()
        b = Path(__file__).parent.joinpath('..', 'sqlite').resolve()
        print(a)
        print(b)
        self.assertEqual(a, b)
        print(Path(__file__).parents)

        print(str(Path(__file__).parent.joinpath("sqlite3.db")))

    def test_win_path(self):
        print(str(Path(__file__).parent.joinpath("sqlite3.db").resolve()))
        print(str(Path(__file__).parent.joinpath("sqlite3.db").absolute()))
        print(str(Path(__file__).parent.joinpath("sqlite3.db").as_posix()))
    def test_win32_url(self):
        sqlite_path = os.getcwd() + '\\dev\\tmp.txt'
        with open(sqlite_path,'r') as my_file:
            print(my_file.read())
            my_file.close()


if __name__ == '__main__':
    unittest.main()
