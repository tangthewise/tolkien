import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_diff1(self):
        node = TextNode("This is text node 1", TextType.BOLD)
        node2 = TextNode("This is text node 2", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_diff2(self):
        node = TextNode("text node", TextType.BOLD)
        node2 = TextNode("text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_diff3(self):
        node = TextNode(None, TextType.BOLD)
        node2 = TextNode(None, TextType.ITALIC)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()