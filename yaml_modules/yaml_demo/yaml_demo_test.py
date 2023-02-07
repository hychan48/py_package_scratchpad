# PyTest
import sys
import pytest
import logging as log
from os.path import expanduser
from pathlib import Path

# so actually pyyaml
import yaml
from yaml import parse


def test_name():
    yaml_filepath = Path().joinpath("yaml_modules", "sample.yml")
    # yaml_stream = open(str(yaml_filepath.resolve()),'r')
    with open(str(yaml_filepath.resolve()), "r") as yaml_stream:
        d_yaml = yaml.safe_load_all(yaml_stream)
        for data in d_yaml:
            log.warning(data)


from yaml.loader import SafeLoader

# https://stackoverflow.com/questions/13319067/parsing-yaml-return-with-line-number
# doesnt quite work im afraid. at least one of the answers
class SafeLineLoader(SafeLoader):
    def construct_mapping(self, node, deep=False):
        mapping = super(SafeLineLoader, self).construct_mapping(node, deep=deep)
        # Add 1 so line numbering starts at 1
        # mapping['__line__'] = node.start_mark.line + 1
        log.critical(node)
        mapping['line'] = node.start_mark.line + 1
        return mapping


def test_line_number():
    yaml_filepath = Path().joinpath("yaml_modules", "sample.yml")
    # yaml_stream = open(str(yaml_filepath.resolve()),'r')
    with open(str(yaml_filepath.resolve()), "r") as yaml_stream:
        d_yaml = yaml.load(yaml_stream, SafeLineLoader)
        for data in d_yaml:
            log.warning(data)


if __name__ == '__main__':
    pytest.main(sys.argv)
