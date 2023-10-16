import json
import unittest

import basic_ops.helpers.convert_to_sets as converter
import basic_ops.helpers.string_helpers as helper
from basic_ops.determinize import determinize


class TestDeterminize(unittest.TestCase):
    def setUp(self):
        self.filenames = [
            # "tests/determinize/determinize_test_cases/determinize_test_1.in",
            "tests/determinize/determinize_test_cases/determinize_test_2.in"
        ]

        # First automaton for each test case
        self.automata = [{}] * len(self.filenames)
        for i in range(len(self.filenames)):
            with open(self.filenames[i]) as f:
                self.automata[i] = json.load(f)

    def test_determinize(self):
        """
        This ensures that all pre-built test cases work.
        """
        for i in range(len(self.automata)):
            # Get the answer
            ans = None
            with open(self.filenames[i][:-2] + "out") as f:
                ans = json.load(f)

            # Get the determinization of the appropriate automaton
            result = determinize(self.automata[i])

            # Print
            # helper.pretty_print(result)
            # helper.pretty_print(ans)

            # Check answer, making sure it's OK if elements not in order
            self.assertEqual(
                converter.convert_to_sets(result), converter.convert_to_sets(ans)
            )
