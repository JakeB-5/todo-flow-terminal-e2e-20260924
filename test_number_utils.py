import unittest

from number_utils import safe_divide


class SafeDivideTests(unittest.TestCase):
    def test_nonzero_division(self):
        for numerator, denominator, expected in (
            (12, 3, 4),
            (-12, 3, -4),
            (12, -3, -4),
            (-12, -3, 4),
            (3, 2, 1.5),
            (0, 5, 0),
        ):
            with self.subTest(numerator=numerator, denominator=denominator):
                self.assertEqual(safe_divide(numerator, denominator), expected)

    def test_zero_denominator_defaults_to_none(self):
        for denominator in (0, 0.0, -0.0):
            with self.subTest(denominator=denominator):
                self.assertIsNone(safe_divide(5, denominator))
        self.assertIsNone(safe_divide(0, 0))

    def test_zero_denominator_preserves_fallback_identity(self):
        fallback = object()
        self.assertIs(safe_divide(5, 0, fallback), fallback)

    def test_nonzero_denominator_ignores_fallback(self):
        self.assertEqual(safe_divide(9, 2, object()), 4.5)

    def test_invalid_operands_propagate_type_error(self):
        for numerator, denominator in (("invalid", 2), (2, None), (2, "")):
            with self.subTest(numerator=numerator, denominator=denominator):
                with self.assertRaises(TypeError):
                    safe_divide(numerator, denominator, fallback="unused")

    def test_division_error_is_not_suppressed(self):
        error = ZeroDivisionError("raised by numerator")

        class FailingNumerator:
            def __truediv__(self, denominator):
                raise error

        with self.assertRaises(ZeroDivisionError) as caught:
            safe_divide(FailingNumerator(), 2, fallback="unused")
        self.assertIs(caught.exception, error)

    def test_denominator_comparison_error_is_not_suppressed(self):
        error = ValueError("comparison failed")

        class FailingDenominator:
            def __eq__(self, other):
                raise error

        with self.assertRaises(ValueError) as caught:
            safe_divide(1, FailingDenominator(), fallback="unused")
        self.assertIs(caught.exception, error)


if __name__ == "__main__":
    unittest.main()
