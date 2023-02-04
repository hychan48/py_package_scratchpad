# content of test_sample.py
# https://docs.pytest.org/en/latest/getting-started.html
# https://docs.pytest.org/en/latest/reference/fixtures.html#fixtures
# https://stackoverflow.com/questions/17801300/how-to-run-a-method-before-all-tests-in-all-classes
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5

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