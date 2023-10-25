import json

import pytest

from structure_validation.automaton_validator import validate


def test_validate_good():
    for i in range(2):
        for char in ["a", "b"]:
            with open(
                f"tests/product/product_test_cases/product_test_{i + 1}{char}_in.json"
            ) as f:
                # Good ones should return true
                assert validate(json.load(f))


@pytest.mark.parametrize(
    "input_num", [pytest.param(i + 1, id=f"Test {i+ 1}") for i in range(4)]
)
def test_validate_bad(input_num: int):
    # Bad ones should give exceptions
    with pytest.raises(Exception):
        automaton_bad = None
        with open(
            f"tests/structure_validation/structure_validation_test_cases/structure_validation_{input_num}_in.json"
        ) as f:
            automaton_bad = json.load(f)
        validate(automaton_bad)
