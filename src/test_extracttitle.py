import unittest

from generate_page import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_simple_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_strips_whitespace(self):
        self.assertEqual(extract_title("#    Hello   "), "Hello")

    def test_title_among_other_blocks(self):
        md = """
Some intro text

# Tolkien Fan Club

Some more text
"""
        self.assertEqual(extract_title(md), "Tolkien Fan Club")

    def test_first_h1_wins(self):
        md = "# First\n\n# Second"
        self.assertEqual(extract_title(md), "First")

    def test_ignores_deeper_headings(self):
        md = "## Not this one\n\n### Nor this\n\n# This one"
        self.assertEqual(extract_title(md), "This one")

    def test_no_h1_raises(self):
        with self.assertRaises(Exception):
            extract_title("## Only an h2\n\nsome text")

    def test_empty_markdown_raises(self):
        with self.assertRaises(Exception):
            extract_title("")


if __name__ == "__main__":
    unittest.main()
