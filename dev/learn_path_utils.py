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

    def test_delete_file(self):
        p_db = Path().joinpath("sqlite", "demo.db")
        # self.assertTrue(p_db.exists())
        print(str(p_db)) # sqlite\demo.db
        print(str(p_db.absolute())) #C:\...\sqlite\demo.db
        p_db.unlink(missing_ok=True)
    def test_path_lib_posix_to_win(self):
        p_db = Path('sqlite/demo.db')
        # p_db = Path('sqlite/../sqlite/demo.db') # relative paths dont work
        # p_db = Path('sqlite/../sqlite/demo.db').resolve() # worrks as expected
        # p_db = Path('sqlite/../sqlite/demo.db') # worrks as expected
        # p_db = Path().joinpath('sqlite/../sqlite/demo.db') # no work
        p_db = Path().joinpath('sqlite/demo.db') # no work
        # print(os.path.split("sqlite/../sqlite/demo.db"))
        # print(os.path.split("sqlite\\..\\sqlite\\demo.db"))
        # print(os.path.split("sqlite\\sqlite\\demo.db"))
        # p_db = Path('~/sqlite/demo.db') # does not auto expand
        # p_db = Path('sqlite/demo.db').absolute() # avoid?
        # p_db = Path('sqlite/demo.db').resolve() # sym links
        # posix gets converted to windows path. which is good
        # https: // docs.python.org / 3 / library / pathlib.html
        from pathlib import PurePath
        # print('hi: ' +PurePath(__file__).name)
        # print('hi: ' +Path(__file__).name)
        self.assertEqual(Path(__file__).name,PurePath(__file__).name)
        print(p_db)
        print(p_db.exists())
    def test_logging(self):
        import logging
        # logging.warning("warning log")
        logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
        # logging.basicConfig(level=logging.DEBUG)

        logging.warning("warning log inside test")
        logging.info('I told you so bla')  # will not print anything


if __name__ == '__main__':
    unittest.main()
