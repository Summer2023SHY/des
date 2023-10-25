import json

import pytest

import basic_ops.helpers.convert_to_sets as converter
import basic_ops.helpers.string_helpers as helper
from basic_ops.controllable import get_controllable


@pytest.mark.parametrize("input_num", [pytest.param(i, id=f"Test {i}") for i in [2]])
def test_controllable(input_num: int):
    # First automaton for each test case
    automaton = None
    with open(
        f"tests/controllable/controllable_test_cases/controllable_test_{input_num}_in.json"
    ) as test_in:
        automaton = json.load(test_in)

    # Get the answer
    ans = None
    with open(
        f"tests/controllable/controllable_test_cases/controllable_test_{input_num}_out.json"
    ) as test_out:
        ans = json.load(test_out)

    # Get the arena for the appropriate automaton
    result = get_controllable(automaton)

    # Print
    # helper.pretty_print(result["states"]["bad"])
    # helper.pretty_print(result)

    # Check answer, making sure it's OK if elements not in order
    assert converter.convert_to_sets(result) == converter.convert_to_sets(ans)
