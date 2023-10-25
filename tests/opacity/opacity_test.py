import json
import unittest

import pytest

import basic_ops.helpers.convert_to_sets as converter
import basic_ops.helpers.string_helpers as helper
from basic_ops.opacity import check_opacity


@pytest.mark.parametrize(
    "input_num", [pytest.param(i + 1, id=f"Test {i + 1}") for i in range(4)]
)
def test_opacity(input_num: int):
    # First automaton for each test case
    automaton = None
    with open(
        f"tests/opacity/opacity_test_cases/opacity_test_{input_num}_in.json"
    ) as test_in:
        automaton = json.load(test_in)

    # Get the answer
    ans = None
    with open(
        f"tests/opacity/opacity_test_cases/opacity_test_{input_num}_out.json"
    ) as test_out:
        ans = json.load(test_out)

    # Check if opaque
    result = check_opacity(automaton)

    # Print
    # helper.pretty_print(result)
    # helper.pretty_print(ans)

    # Check answer, making sure it's OK if elements not in order
    assert converter.convert_to_sets(result) == converter.convert_to_sets(ans)
