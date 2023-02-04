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
    def test_mkdir(self):
        import os
        from pathlib import Path
        ## hard coded first
        # folderPath = 'dev\\tmpFolder'
        folderPath = str(Path().joinpath('dev','tmpFolder'))
        print(folderPath)
        # old way
        # if(not os.path.exists(folderPath)): os.mkdir(folderPath)
        # new way
        # https: // www.programiz.com / python - programming / examples / create - nested - directories
        Path().joinpath('dev', 'tmpFolder').mkdir(parents=True, exist_ok=True)
        # repeated to make sure no error
        Path().joinpath('dev', 'tmpFolder').mkdir(parents=True, exist_ok=True)
        self.assertTrue(os.lstat(folderPath))
        self.assertTrue(Path().joinpath('dev', 'tmpFolder').is_dir())
        # Path().joinpath('dev', 'tmpFolder')
        import shutil
        shutil.rmtree(str(Path().joinpath('dev', 'tmpFolder')))

        self.assertTrue(os.lstat(folderPath))

    def test_expand_user_win(self):
        # from pathlib.Path import expanduser
        from os.path import expanduser
        home = expanduser('~')
        print(home)
        self.assertTrue(True)




if __name__ == '__main__':
    unittest.main()
