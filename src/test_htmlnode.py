import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_empty_node_to_html(self):        
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_basic_props_node_to_html(self):        
        node = HTMLNode(props={"class": "div"})        
        self.assertEqual(node.props_to_html(), " class=\"div\"")

    def test_multiple_props_node_to_html(self):        
        node = HTMLNode(props={"class": "div", "id": "main"})        
        self.assertEqual(node.props_to_html(), " class=\"div\" id=\"main\"")
        
        



if __name__ == "__main__":
    unittest.main()