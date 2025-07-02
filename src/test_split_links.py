import unittest

from textnode import TextNode, TextType
from textnodefunctions import split_nodes_link


class TestSplitTextOnLinks(unittest.TestCase):    

    def test_splittest_Having_an_empty_TextNode_with_matching_delimiter_then_should_return_an_empty_result(self):
        test_text_node = TextNode("", TextType.TEXT)
                
        result = split_nodes_link([test_text_node])
        
        self.assertEqual(len(result), 0, "there is no text to return")