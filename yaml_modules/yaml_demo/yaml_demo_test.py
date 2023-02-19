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
class SafeLineLoaderOld(SafeLoader):
    def construct_mapping(self, node, deep=False):
        # mapping = super(SafeLineLoader, self).construct_mapping(node, deep=deep)
        mapping = super().construct_mapping(node, deep=deep)
        # Add 1 so line numbering starts at 1
        # mapping['__line__'] = node.start_mark.line + 1
        log.critical(node)
        mapping['line'] = node.start_mark.line + 1
        return mapping

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
        node = super().compose_node(parent, index) # max call stack
        node.__line__ = line + 1 # line numbers start at 0 so + 1
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
        mapping['__line__'] = node.__line__ # parent line number start. so each mapping is per object
        # log.critical(mapping) # only runs once... per mapping... so it doenst work properly
        return mapping

import json
def test_line_number():
    yaml_filepath = Path().joinpath("yaml_modules", "sample.yml")
    # yaml_stream = open(str(yaml_filepath.resolve()),'r')
    with open(str(yaml_filepath.resolve()), "r") as yaml_stream:
        # d_yaml = yaml.load_all(yaml_stream, SafeLineLoader)
        d_yaml = yaml.load(yaml_stream, SafeLineLoader)
        # d_yaml = yaml.load_all(yaml_stream, SafeLineLoader) # generator class..
        print(type(d_yaml)) # dict...

        with open(str(Path("yaml_modules/yaml_demo/d_yaml.json")), "w") as outfile:
            json.dump(d_yaml, outfile, indent=2)

        for data in d_yaml:
            log.info(data)
            # log.warning(data.__line__)


if __name__ == '__main__':
    pytest.main(sys.argv)
