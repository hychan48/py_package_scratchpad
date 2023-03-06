# PyTest
import sys
import pytest
import logging as log
# import platform # not useful for learning how to get the os
import os # not useful for learning how to get the os

# https://docs.pytest.org/en/7.1.x/how-to/skipping.html
@pytest.mark.skipif(not os.name == 'nt' , reason="Window only")
def test_is_windows():
    system_name = os.name
    # also sys.platform
    # log.warning(system_name)
    # log.warning(sys.platform)
    # https: // docs.python.org / 3 / library / sys.html  # sys.platform
    assert system_name == 'nt'
@pytest.mark.skipif(not os.name == 'nt' , reason="Window only")
def test_windows_env():
    # Local Python Env. seems to work
    # might need to test for overriding
    # env_test = os.system('set ENV_TEST') # will print error to console
    env_test = os.system('set ENV_TEST 2 > nul')
    log.warning(env_test)
    assert env_test == 1
    # https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5#:~:text=To%20set%20and%20get%20environment%20variables%20in%20Python%20you%20can,Get%20environment%20variables%20USER%20%3D%20os.
    os.environ['ENV_TEST'] = 'hello world'
    # os.unsetenv()
    env_test = os.system('set ENV_TEST 1 > nul')
    assert env_test == 0
    # log.warning(env_test)

@pytest.mark.skipif(not os.name == 'posix' , reason="linux only")
def test_is_ubuntu():
    system_name = os.name
    assert system_name == 'posix'



if __name__ == '__main__':
    pytest.main(sys.argv)
