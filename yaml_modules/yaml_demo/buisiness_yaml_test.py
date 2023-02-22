# PyTest
import sys
import pytest
import logging as log
from os.path import expanduser
from pathlib import Path

# so actually pyyaml
import yaml
from yaml import parse
from yaml.loader import SafeLoader
import json


def test_name():
    yaml_filepath = Path().joinpath("yaml_modules", "sample.yml")
    # yaml_stream = open(str(yaml_filepath.resolve()),'r')
    with open(str(yaml_filepath.resolve()), "r") as yaml_stream:
        d_yaml = yaml.safe_load_all(yaml_stream)
        for data in d_yaml:
            log.warning(data)


# https://realpython.com/python-yaml/#dump-custom-data-types
# https://github.com/yaml/pyyaml/blob/8cdff2c80573b8be8e8ad28929264a913a63aa33/lib/yaml/composer.py
class SafeLineLoader(SafeLoader):
    def compose_node(self, parent, index):
        # the line number where the previous token has ended (plus empty lines)
        line = self.line
        column = self.column
        log.warning(f"compose_node line: {line + 1}")
        log.warning(f"compose_node col: {column + 1}")
        # node = self.compose_node(parent, index) # max call stack
        # node = super(SafeLineLoader, self).compose_node(parent, index) # max call stack
        node = super().compose_node(parent, index)  # max call stack
        node.__line__ = line + 1  # line numbers start at 0 so + 1
        # log.critical(line + 1) # gets run per node
        return node

    # nothing of interest
    def compose_scalar_node(self, anchor):
        # log.error(anchor)
        node = super().compose_scalar_node(anchor)
        # log.critical(node)
        return node

    def construct_object(self, node, deep=False):
        # wrong place to get line and column from self.
        # line = self.line
        # column = self.column
        # log.warning(f"construct_object line: {line}")
        # log.warning(f"construct_object col: {column}")
        obj = super().construct_object(node, deep=deep)
        # obj.hi='world'
        # log.critical(obj)
        return obj
        # key = id(obj)
        # if key in self.locations:
        #     self.locations[key] = None
        # else:
        #     self.locations[key] = node._myloader_location
        # return obj

    # missing construct_object? seems better ref:
    # https://github.com/yaml/pyyaml/issues/456
    # construct_object instead of mapping
    def construct_mapping(self, node, deep=False):
        # mapping = super(SafeLineLoader, self).construct_mapping(node, deep=deep)
        # mapping = self.construct_mapping(node, deep=deep)
        mapping = super(SafeLineLoader, self).construct_mapping(node, deep=deep)
        mapping['__line__'] = node.__line__  # parent line number start. so each mapping is per object
        # log.critical(mapping) # only runs once... per mapping... so it doenst work properly
        return mapping

    # todo look into compose_mapping_node(self, anchor):


def test_line_number():
    yml_filename = "business_sample.yml"
    yaml_filepath = Path().joinpath("yaml_modules", yml_filename)
    # yaml_stream = open(str(yaml_filepath.resolve()),'r')
    with open(str(yaml_filepath.resolve()), "r") as yaml_stream:
        # d_yaml = yaml.load_all(yaml_stream, SafeLineLoader)
        d_yaml = yaml.load(yaml_stream, SafeLineLoader)
        # d_yaml = yaml.load_all(yaml_stream, SafeLineLoader) # generator class..
        print(type(d_yaml))  # dict...

        with open(str(Path(f"yaml_modules/yaml_demo/{yml_filename}.json")), "w") as outfile:
            json.dump(d_yaml, outfile, indent=2)

        for data in d_yaml:
            log.info(data)
            # log.warning(data.__line__)


def test_dataclass():
    from dataclasses import dataclass
    # https://www.w3schools.com/python/python_datatypes.asp
    # https://docs.python.org/3/library/dataclasses.html

    # try nested class
    @dataclass(init=True)
    class YamlItems:
        key: str # or maybe complex
        value: complex = 0 # or maybe a nested class or list or something? NoneType?
        line: int = 0
        column: int = 0



    a = YamlItems("a")
    log.warning(a)
    # @dataclass
    # class C:
    #      mylist: list[Point]


if __name__ == '__main__':
    pytest.main(sys.argv)
