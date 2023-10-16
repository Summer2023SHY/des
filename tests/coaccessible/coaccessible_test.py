import json
import unittest

import basic_ops.helpers.convert_to_sets as converter
import basic_ops.helpers.string_helpers as helper
from basic_ops.coaccessible import get_coaccessible


class TestCoaccessible(unittest.TestCase):
    def setUp(self):
        self.filenames = [
            "tests/coaccessible/coaccessible_test_cases/coaccessible_1_in.json",
            "tests/coaccessible/coaccessible_test_cases/coaccessible_2_in.json",
        ]

        # First automaton for each test case
        self.automata = [{}] * len(self.filenames)
        for i in range(len(self.filenames)):
            with open(self.filenames[i]) as f:
                self.automata[i] = json.load(f)

    def test_coaccessible(self):
        """
        This ensures that all pre-built test cases work.
        """
        for i in range(len(self.automata)):
            # Get the answer
            ans = None
            with open(self.filenames[i][:-7] + "out.json") as f:
                ans = json.load(f)

            # Get the arena for the appropriate automaton
            result = get_coaccessible(self.automata[i])

            # Print
            # helper.pretty_print(result)

            # Check answer, making sure it's OK if elements not in order
            self.assertEqual(
                converter.convert_to_sets(result), converter.convert_to_sets(ans)
            )
