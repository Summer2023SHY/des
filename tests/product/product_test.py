import json

import pytest

import basic_ops.helpers.convert_to_sets as converter
import basic_ops.helpers.string_helpers as helper
from basic_ops.product import product


@pytest.mark.parametrize("input_num", [pytest.param(i, id=f"Test {i}") for i in [1, 2]])
def test_product(input_num: int):
    # First automaton for each test case
    automaton1 = None
    with open(
        f"tests/product/product_test_cases/product_test_{input_num}a_in.json"
    ) as test_in1:
        automaton1 = json.load(test_in1)
    # Second automaton for each test case
    automaton2 = None
    with open(
        f"tests/product/product_test_cases/product_test_{input_num}b_in.json"
    ) as test_in2:
        automaton2 = json.load(test_in2)

    # Get the answer
    ans = None
    with open(
        f"tests/product/product_test_cases/product_test_{input_num}_out.json"
    ) as test_out:
        ans = json.load(test_out)

    # Get the product of the appropriate automata
    result = product([automaton1, automaton2])

    # Print
    # helper.pretty_print(result)
    # helper.pretty_print(ans)

    # Check answer, making sure it's OK if elements not in order
    assert converter.convert_to_sets(result) == converter.convert_to_sets(ans)
