import json

import pytest

import basic_ops.helpers.convert_to_sets as converter
import basic_ops.helpers.string_helpers as helper
from arenas.construct_arena import construct_arena


@pytest.mark.parametrize("input_num", [pytest.param(i, id=f"Test {i}") for i in [1, 3]])
def test_construct_arena(input_num: int):
    # First automaton for each test case
    automaton = None
    with open(
        f"tests/arenas/construct_arena_test_cases/arenas_test_{input_num}_in.json"
    ) as test_in:
        automaton = json.load(test_in)
    # Get the answer
    ans = None
    with open(
        f"tests/arenas/construct_arena_test_cases/arenas_test_{input_num}_out.json"
    ) as test_out:
        ans = json.load(test_out)

    # Get the arena for the appropriate automaton
    result = construct_arena(automaton)

    # Print
    # helper.pretty_print(result["states"]["bad"])
    # helper.pretty_print(result)

    # Check answer, making sure it's OK if elements not in order
    assert converter.convert_to_sets(result) == converter.convert_to_sets(ans)
