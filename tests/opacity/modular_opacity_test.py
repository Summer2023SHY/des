import json

import pytest

import basic_ops.helpers.convert_to_sets as converter
import basic_ops.helpers.string_helpers as helper
from modular_opacity.heuristics import least_new_heuristic, most_shared_heuristic
from modular_opacity.modular_opacity_verification import check_modular_opacity
from structure_validation.automaton_validator import validate


@pytest.mark.parametrize("input_num", [pytest.param(i, id=f"Test {i}") for i in [1, 2]])
def test_modular_opacity(input_num: int):
    answer = input_num % 2 == 0
    filenames = [
        f"tests/opacity/modular_opacity_test_cases/modular_test_{input_num}-{i}_in.json"
        for i in [1, 2]
    ]

    # First automaton for each test case
    automata = [{}] * len(filenames)
    for i in range(len(filenames)):
        with open(filenames[i]) as f:
            automata[i] = json.load(f)
            validate(automata[i])

    # Check if opaque
    result = check_modular_opacity(automata)
    assert result == answer
    result = check_modular_opacity(
        automata,
        heuristic=most_shared_heuristic,
    )
    assert result == answer
    result = check_modular_opacity(
        automata,
        heuristic=least_new_heuristic,
    )
    assert result == answer
