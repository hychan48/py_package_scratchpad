# content of test_sample.py
# https://docs.pytest.org/en/latest/getting-started.html
# https://docs.pytest.org/en/latest/reference/fixtures.html#fixtures
# https://stackoverflow.com/questions/17801300/how-to-run-a-method-before-all-tests-in-all-classes
def inc(x):
    return x + 1


import logging

# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.basicConfig(filename='example.log', filemode='w', encoding='utf-8', level=logging.DEBUG)


# logging.basicConfig(level=logging.DEBUG)
def test_answer():
    assert inc(4) == 5


import pytest


class TestClassDemoInstance:
    value = 0

    @pytest.fixture(scope="session", autouse=True)
    def pytest_configure(self):
        print('starting on session')
        # with capsys.disabled():
        #     print("this output will not be captured and go straight to sys.stdout"

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        self.value = 1
        assert self.value == 1

    def test_logging(self):
        # import logging
        #
        # # logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
        # logging.basicConfig(filename='example.log', filemode='w', encoding='utf-8', level=logging.DEBUG)
        # # logging.basicConfig(level=logging.DEBUG)
        # level name
        # https: // docs.python.org / 3 / library / logging.html
        logging.debug("debug pytest")
        logging.info('info pytest')
        logging.warning('warning pytest')
        logging.error('error pytest')
        logging.critical('critical pytest')


if __name__ == '__main__':
    import sys

    pytest.main(sys.argv)
