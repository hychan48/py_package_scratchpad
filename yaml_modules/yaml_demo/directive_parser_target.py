# PyTest
import sys
import pytest
import logging as log

# Directive @@target string to Python Dict
# easiest way imo is to use YAML Parser, after = substitution
# Feel free to manually parse it as well. initial demo:

# Purposely implemented in a deliberately thorough way.
# Broke down the code as small as possible
# i.e many individual functions / unit tests.
# Language parsers are tricky

# --------------
import yaml
import re


# X Steps using yaml - assuming {{ }} already
# Separte functions for easier validating. in the future
# Strings are from users. Expect the unexpected
# 1. Replace Colon With Equals = to :
#   note needs space after colon for yaml to work... unt ideal
# 2. Remove Single from start and end { }
# 3.

#
def directive_replace_equal_with_colon(string_target_input: str):
    # quick and dirty - better regex might be needed
    # replace "=s" to "= s"
    # replace all "=" to ":"
    # maybe combine regex later
    # re.sub(pattern, replacement, string, count=0, flags=0)
    spaced_equals = re.sub(r"=(\S)", r"= \1", string_target_input)  # replace all

    return spaced_equals.replace("=", ":")  # replace all
    # return string_target_input.replace("=", ":")  # replace all


def directive_quote_at_at(string_target_input: str, at_at: str = "@@target"):
    # quick and dirty - regex might be needed / triming
    return string_target_input.replace(at_at, f"'{at_at}'")  # replace all


def directive_parser_target(string_target_input: str):
    # assuming string_target_input already semi-validated and @@target directive
    # input is from user. expect the unexpected
    log.warning('hi')


# --------------

# insert here more unit test class for each def
class TestA:
    pass


class TestDirectiveReplaceEqualWithColon:
    @pytest.mark.parametrize("str_input,expected", [
        ("hi=Hi", "hi: Hi"),
        ("hi= Hi", "hi: Hi"),
        ("start=1, end=2", "start: 1, end: 2"),  # multiple, still works
    ])
    def test_capital_case_array(self, str_input, expected):
        assert directive_replace_equal_with_colon(str_input) == expected


class TestDirectiveParserTarget:
    def test_hard_coded_single_target_basic(self):
        # assuming string is semi-validated as a directive string value
        # Pseudo Code
        string_target_input = "{{ @@target: guest-lnx, name-prefix=ub1, start=1, end=2, parallel=true, interval=5s, blocking=true }}"
        # 1. Replace Colon With Equals = to :. note needs space after colon
        replace_colon_with_equals = "{{ @@target: guest-lnx, name-prefix: ub1, start: 1, end: 2, parallel: true, interval: 5s, blocking: true }}"
        # 2. quote @@target
        quote_at_at_target = "{{ '@@target': guest-lnx, name-prefix: ub1, start: 1, end: 2, parallel: true, interval: 5s, blocking: true }}"
        # 3. Remove Single from start and end { }
        extract_to_yaml_obj_str = "{ '@@target': guest-lnx, name-prefix: ub1, start: 1, end: 2, parallel: true, interval: 5s, blocking: true }"
        # 4. Run pyyaml safeloader
        dict_target_directive = yaml.safe_load(extract_to_yaml_obj_str)
        assert dict_target_directive == {'@@target': 'guest-lnx', 'name-prefix': 'ub1', 'start': 1, 'end': 2,
                                         'parallel': True, 'interval': '5s', 'blocking': True}

    def test_single_target_basic(self):
        s_input = "{{ @@target: guest-lnx, name-prefix=ub1, start=1, end=2, parallel=true, interval=5s, blocking=true }}"
        # Pseudo Code
        log.warning("hi")

    def test_multi_target_basic(self):
        s_input = "{{ @@target: [guest-lnx], name-prefix=ub1, start=1, end=2, parallel=true, interval=5s, blocking=true }}"
        # Pseudo Code
        log.warning("hi")

    # @pytest.mark.parametrize("str_input,expected", [
    #     ("hello", "Hello"),
    #     ("world", "World"),
    # ])


if __name__ == '__main__':
    pytest.main(sys.argv)
