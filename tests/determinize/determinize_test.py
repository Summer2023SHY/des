import json

import pytest

import basic_ops.helpers.convert_to_sets as converter
import basic_ops.helpers.string_helpers as helper
from basic_ops.determinize import determinize


@pytest.mark.parametrize("input_num", [pytest.param(i, id=f"Test {i}") for i in [1, 2]])
def test_determinize(input_num: int):
    if input_num == 1:
        # Original unittest version of test skipped this input
        pytest.skip()
    # First automaton for each test case
    automaton = None
    with open(
        f"tests/determinize/determinize_test_cases/determinize_test_{input_num}_in.json"
    ) as test_in:
        automaton = json.load(test_in)

    # Get the answer
    ans = None
    with open(
        f"tests/determinize/determinize_test_cases/determinize_test_{input_num}_out.json"
    ) as test_out:
        ans = json.load(test_out)

    # Get the determinization of the appropriate automaton
    result = determinize(automaton)

    # Print
    # helper.pretty_print(result)
    # helper.pretty_print(ans)

    # Check answer, making sure it's OK if elements not in order
    assert converter.convert_to_sets(result) == converter.convert_to_sets(ans)
