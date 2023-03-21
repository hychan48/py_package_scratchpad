# PyTest
import sys
import pytest
import logging as log

import dataclasses
from dataclasses import dataclass

"""
Keep in mind
the difference between a dict and an object!
https://www.w3schools.com/python/python_dictionaries.asp
https://docs.python.org/3/library/dataclasses.html
also try dataclasses

i think more than one level. doesnt work?
"""

# this is a json. it's not really a dictionary if you think about it
sample_a_dict = dict(a={"b": {"c": "d"}})
sample_a_str = {"a": {"b": {"c": "d"}}}


# maybe add dotty to make life easier and make this its own package
@dataclass()
class Object:
    combined: dict=None

    # key: str
    # value: object
    # x: list = field(default_factory=list)
    # def __init__(self, key: str, value: object, combined: dict = None):  # doesnt have overloading
    def __init__(self, key: str, value: object):  # doesnt have overloading
        # name_keys:list=None
        # name_keys = ['a'] if name_keys is None else name_keys
        # if combined is not None:
        #     self.combined = combined # maybe deep copy?
        #     # problem here is i dont set the key or value...
        #     # need to create a combined option or something
        #     # todo
        #     return

        self.key = key
        self.value = value
        self.combined = dict([(key, value)])



    # doesnt change the asdict... interesting
    # def __repr__(self):
    #     return ""
    def to_dict(self):  # *, dict_factory
        # need to modify this?
        value = self.value
        # is_obj = isinstance(value,self.__class__) # same as comparing to "Object"
        if isinstance(value,self.__class__):
            value = value.to_dict()
        d = dict([(self.key, value)])
        return d
        # return dataclasses.asdict(self)


@dataclass()
class ABCD:
    pass


assert sample_a_str == sample_a_dict


def test_name():
    """
    custom name
    :return:
    """
    name = 'hello'
    a = dict([(name, 'value')])
    b = dict([("name", 'value')])
    # d = dict([(a,b)])
    d = dict(a | b)  # 3.9 syntax

    log.warning(d)
    log.warning("hi")


"""try .update a bit more. it has different syntax"""


def test_dataclass_obj():
    value = Object('b', 'c')
    a = Object("a", value)
    log.warning(a.to_dict())
    # WARNING  root:dict_tutorial.py:63 {'key': 'a', 'value': {'b': 'c'}}
    # we want a:b:c


@pytest.mark.parametrize("test_input,expected", [
    ("b", {'a': 'b'}),
    (dict(b='c'), {'a': {'b': 'c'}}),
    (Object('b','c'), {'a': {'b': 'c'}}),
])
def test_dataclass_obj_multi(test_input, expected):
    try:
        value = test_input
        a = Object("a", value)
        actual = a.to_dict()
        assert actual == expected
    except AssertionError as aex:
        log.warning(actual)
        raise aex
    except Exception as ex:
        raise ex


if __name__ == '__main__':
    pytest.main(sys.argv)
