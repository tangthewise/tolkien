import unittest

from split_nodes import markdown_to_html_node


class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_headings(self):
        md = """
# Heading 1

### Heading 3 with **bold**
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h3>Heading 3 with <b>bold</b></h3></div>",
        )

    def test_quote(self):
        md = """
> This is a quote
> spanning _two_ lines
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote spanning <i>two</i> lines</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- item one
- item **two**
- item three
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>item one</li><li>item <b>two</b></li><li>item three</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. item one
2. item _two_
3. item three
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>item one</li><li>item <i>two</i></li><li>item three</li></ol></div>",
        )

    def test_all_block_types_together(self):
        md = """
# My Document

This is a **paragraph** with some _italic_ text.

> A quote block

- list item one
- list item two

1. first
2. second

```
raw _code_ **here**
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div>"
            "<h1>My Document</h1>"
            "<p>This is a <b>paragraph</b> with some <i>italic</i> text.</p>"
            "<blockquote>A quote block</blockquote>"
            "<ul><li>list item one</li><li>list item two</li></ul>"
            "<ol><li>first</li><li>second</li></ol>"
            "<pre><code>raw _code_ **here**\n</code></pre>"
            "</div>",
        )


if __name__ == "__main__":
    unittest.main()
