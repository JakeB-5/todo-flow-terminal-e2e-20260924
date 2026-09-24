import unittest

from text_utils import compact


class CompactTests(unittest.TestCase):
    def test_mixed_spaces_tabs_and_newlines(self):
        self.assertEqual(compact("alpha  \t beta\n\r\ngamma\t\tdelta"),
                         "alpha beta gamma delta")

    def test_trims_edges(self):
        self.assertEqual(compact(" \t\n alpha beta \r\n "), "alpha beta")

    def test_empty_input(self):
        self.assertEqual(compact(""), "")

    def test_whitespace_only_input(self):
        for text in (" ", "\t\n\r\v\f", " \t\n ", "\u00a0\u2003\u202f\u3000"):
            with self.subTest(text=text):
                self.assertEqual(compact(text), "")

    def test_unicode_whitespace(self):
        self.assertEqual(compact("\u3000alpha\u00a0\u2003beta\u202fgamma\u3000"),
                         "alpha beta gamma")

    def test_preserves_non_whitespace_text(self):
        for text in ("Hello, world!", "café 한글", "a_b-123.!", "a\u200bb"):
            with self.subTest(text=text):
                self.assertEqual(compact(text), text)


if __name__ == "__main__":
    unittest.main()
