import unittest

from textnode import TextNode, TextType
from textnodefunctions import text_node_to_html_node, split_nodes_delimiter


class TestTextNodeFunctions(unittest.TestCase):    

    def test_text_tohtml(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")        

    def test_bold_tohtml(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")
       


if __name__ == "__main__":
    unittest.main()