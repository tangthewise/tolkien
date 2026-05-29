import unittest

from split_nodes import split_nodes_delimiter

class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_with_basic_bold_delimiter(self):
        from textnode import TextNode, TextType

        old_nodes = [TextNode("This is a *bold* text", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "*", TextType.BOLD)

        expected_nodes = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]

        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_with_multiple_bold_delimiters(self):
        from textnode import TextNode, TextType

        old_nodes = [TextNode("This is *bold* and this is *also bold*", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "*", TextType.BOLD)

        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and this is ", TextType.TEXT),
            TextNode("also bold", TextType.BOLD)
        ]

        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_with_no_delimiters(self):
        from textnode import TextNode, TextType

        old_nodes = [TextNode("This is a plain text", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "*", TextType.BOLD)

        expected_nodes = [TextNode("This is a plain text", TextType.TEXT)]

        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_With_whole_text_as_bold(self):
        from textnode import TextNode, TextType

        old_nodes = [TextNode("*This is bold text*", TextType.TEXT)]
        
        new_nodes = split_nodes_delimiter(old_nodes, "*", TextType.BOLD)
        
        expected_nodes = [TextNode("This is bold text", TextType.BOLD)]
        
        

    def test_split_nodes_delimiter_no_pairs(self):
        from textnode import TextNode, TextType

        old_nodes = [TextNode("This is a *bold text", TextType.TEXT)]
        
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter(old_nodes, "*", TextType.BOLD)
        
        self.assertIn("Delimiter '*' not found as a matching pair", str(context.exception))