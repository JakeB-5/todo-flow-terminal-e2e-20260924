import unittest

from parity_utils import is_even


class IsEvenTests(unittest.TestCase):
    def test_zero_and_even_integers_return_true(self):
        for value in (0, 2, 4, 100, -2, -4, -100):
            with self.subTest(value=value):
                self.assertIs(is_even(value), True)

    def test_odd_integers_return_false(self):
        for value in (1, 3, 99, -1, -3, -99):
            with self.subTest(value=value):
                self.assertIs(is_even(value), False)


if __name__ == "__main__":
    unittest.main()
