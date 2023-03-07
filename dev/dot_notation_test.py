# PyTest
import sys
import pytest
import logging as log

from types import SimpleNamespace
from dotty_dict import dotty

import json
from pathlib import Path


# https://stackoverflow.com/questions/16279212/how-to-use-dot-notation-for-dict-in-python
# https://pypi.org/project/dotty-dict/
def test_raw():
    d = {'key1': 'value1', 'key2': 'value2'}
    n = SimpleNamespace(**d)
    out = n.key1
    # log.warning(out)
    assert out == 'value1'


def test_file():
    with open(str(Path("dev/json_files/data.json"))) as json_file:
        data = json.load(json_file)
        n = SimpleNamespace(**data)
        out = n.oData
        out = n.oData['data']
        # out = n.oData.data # fails for nested
        log.warning(out)


def test_dotty_dict_demo():
    dot = dotty({'plain': {'old': {'python': 'dictionary'}}})
    out = dot['plain.old.python']
    # log.warning(out)
    assert out == 'dictionary'


def test_dotty_dict_file():
    with open(str(Path("dev/json_files/data.json"))) as json_file:
        data = json.load(json_file)
        dot = dotty(data)
        out = dot['arrayItems.0']
        # log.warning(out)
        assert out == 1


@pytest.mark.parametrize("test_input,expected", [
    ("strHello", "Hello"),
    ("oData.data", "data field"),
    ("arrayItems.0", 1),
    # pytest.param('skip', "skip", marks=pytest.mark.xfail(reason="but why")),
])
def test_dotty_multi(test_input, expected):
    with open(str(Path("dev/json_files/data.json"))) as json_file:
        data = json.load(json_file)
        dot = dotty(data)
        out = dot[test_input]
        # log.warning(out)
        assert out == expected


if __name__ == '__main__':
    pytest.main(sys.argv)
