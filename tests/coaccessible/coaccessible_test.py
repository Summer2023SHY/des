import json

import pytest

import basic_ops.helpers.convert_to_sets as converter
import basic_ops.helpers.string_helpers as helper
from basic_ops.coaccessible import get_coaccessible


@pytest.mark.parametrize("input_num", [pytest.param(i, id=f"Test {i}") for i in [1, 2]])
def test_coaccessible(input_num: int):
    # First automaton for each test case
    automaton = None
    with open(
        f"tests/coaccessible/coaccessible_test_cases/coaccessible_{input_num}_in.json"
    ) as test_in:
        automaton = json.load(test_in)

    # Get the answer
    ans = None
    with open(
        f"tests/coaccessible/coaccessible_test_cases/coaccessible_{input_num}_out.json"
    ) as test_out:
        ans = json.load(test_out)

    # Get the arena for the appropriate automaton
    result = get_coaccessible(automaton)

    # Print
    # helper.pretty_print(result)

    # Check answer, making sure it's OK if elements not in order
    assert converter.convert_to_sets(result) == converter.convert_to_sets(ans)
