from leafnode import LeafNode
from parentnode import ParentNode
import unittest

class TestParentNode(unittest.TestCase):
    def test_parent_to_html_div(self):
        node = ParentNode("div", [LeafNode("p", "Hello, world!")])
        self.assertEqual(node.to_html(), "<div><p>Hello, world!</p></div>")

    def test_parent_to_html_div_with_props(self):
        node = ParentNode("div", [LeafNode("p", "Hello, world!")], props={"class": "container"})
        self.assertEqual(node.to_html(), '<div class="container"><p>Hello, world!</p></div>')

    def test_parent_to_html_no_tag(self):
        node = ParentNode("", [LeafNode("p", "Hello, world!")])        
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_to_html_empty_children(self):
        node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            node.to_html()
