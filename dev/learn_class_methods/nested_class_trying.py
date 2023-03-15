# import pytest
import logging as log

"""
Base Class
* States

A uses States
B uses States

Combined Class
C is both A and B
* pretty sure this wont work

"""


class Base:
    def __init__(self):
        self.states = {

        }
        self.some_str = 'some_base'


class A(Base):
    def __init__(self):
        # pass # will fail
        super().__init__()  # need this  for it not to fail

    def log_a(self):
        log.warning("a :" + self.some_str)

    def nothing_warning(self):
        """no static warning if I do this"""

    def warning_using_pass(self):
        # interesting... no warning yet
        pass


class B(Base):
    def log_b(self):
        log.warning("b :" + self.some_str)


class C(A, B):
    def log_c(self):
        log.warning("c :" + self.some_str)

    def __init__(self, someparam='s'):
        super().__init__()  # actual syntax or A.__init__
        self.someparam = someparam

    #     super().__init__(self)
    #     # default works?


def test_main():
    log.warning("test_main")
    c = C()  # works.. but default __init is?
    c.log_a()
    c.log_b()

    c.some_str = ' new some str '
    c.log_a()
    c.log_b()
