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




        # log.warning(f"compose_node line: {line + 1}")
        # log.warning(f"compose_node col: {column + 1}")

        # node = self.compose_node(parent, index) # max call stack
        # node = super(SafeLineLoader, self).compose_node(parent, index) # max call stack
        node = super().compose_node(parent, index) # max call stack

        # line = node.start_mark.line
        # column = node.start_mark.column

        # if it's nested. line doesnt need to be appended by 1... interesting
        # so any nested is off by line 1
        # node.__line__ = line + 1  # line numbers start at 0 so + 1
        node.__line__ = line + 1  # using start_mark... or end_mark. doesnt need + 1? . no it doesnt help.
        # if they're all equal... it's minue one?. 17 is the wrong one...
        # log.warning(f"parent: {parent}")

        # Investigating why line number is off by 1 for non nested values
        # Results using self.line without appending...
        # line start.line end.line
        # WARNING  root:yaml_demo_test.py:74 hello_1: 0 0 0 # needs to be + 1. when they're all equal
        # WARNING  root:yaml_demo_test.py:66 five: 5 4 4 # line is correct w/0 + 1
        # WARNING  root:yaml_demo_test.py:69 14: 14 13 13 #
        # WARNING  root:yaml_demo_test.py:72 17.1: 16 16 16 # +1 is needed

        if(node.value == 'hello_1'):
            # log.warning(f"parent: {parent}")
            log.warning(f"hello_1: {line} {node.start_mark.line} {node.end_mark.line}")
        if(node.value == 'five'):
            # log.warning(f"parent: {parent}")
            log.warning(f"five: {line} {node.start_mark.line} {node.end_mark.line}")
        elif(node.value == '14'):
            # log.warning(f"parent: {parent}")
            log.warning(f"14: {line} {node.start_mark.line} {node.end_mark.line}")
        elif(node.value == '17.1'):
            # log.warning(f"parent: {parent}")
            log.warning(f"17.1: {line} {node.start_mark.line} {node.end_mark.line}")
        # if(type(node.value) == str):
        #     log.warning(f"compose_node value line col: \"{node.value}\" {line + 1}:{column + 1}")

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

    # todo look into compose_mapping_node(self, anchor):

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
