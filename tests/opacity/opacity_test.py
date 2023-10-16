import json
import unittest

import basic_ops.helpers.convert_to_sets as converter
import basic_ops.helpers.string_helpers as helper
from basic_ops.opacity import check_opacity


class TestOpacity(unittest.TestCase):
    def setUp(self):
        self.filenames = [
            "tests/opacity/opacity_test_cases/opacity_test_1_in.json",
            "tests/opacity/opacity_test_cases/opacity_test_2_in.json",
            "tests/opacity/opacity_test_cases/opacity_test_3_in.json",
            "tests/opacity/opacity_test_cases/opacity_test_4_in.json",
        ]

        # First automaton for each test case
        self.automata = [{}] * len(self.filenames)
        for i in range(len(self.filenames)):
            with open(self.filenames[i]) as f:
                self.automata[i] = json.load(f)

    def test_opacity(self):
        """
        This ensures that all pre-built test cases work.
        """
        for i in range(len(self.automata)):
            # Get the answer
            ans = None
            with open(self.filenames[i][:-7] + "out.json") as f:
                ans = json.load(f)

            # Check if opaque
            result = check_opacity(self.automata[i])

            # Print
            # helper.pretty_print(result)
            # helper.pretty_print(ans)

            # Check answer, making sure it's OK if elements not in order
            self.assertEqual(
                converter.convert_to_sets(result), converter.convert_to_sets(ans)
            )
