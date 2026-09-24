import unittest

from sequence_utils import ordered_unique


class OrderedUniqueTests(unittest.TestCase):
    def test_interleaved_duplicates_keep_first_occurrence_order(self):
        self.assertEqual(
            ordered_unique([3, 1, 3, 2, 1, 4, 2, 3]),
            [3, 1, 2, 4],
        )

    def test_empty_input(self):
        self.assertEqual(ordered_unique([]), [])

    def test_already_unique_input(self):
        values = [4, 2, 9, 1]
        result = ordered_unique(values)
        self.assertEqual(result, [4, 2, 9, 1])
        self.assertIsNot(result, values)

    def test_original_input_is_unchanged(self):
        values = [3, 1, 3, 2, 1]
        original = values.copy()
        result = ordered_unique(values)
        self.assertEqual(values, original)
        self.assertEqual(result, [3, 1, 2])
        self.assertIsNot(result, values)

    def test_mixed_hashable_values(self):
        self.assertEqual(
            ordered_unique(["b", (1, 2), None, "b", 7, (1, 2), None]),
            ["b", (1, 2), None, 7],
        )


if __name__ == "__main__":
    unittest.main()
