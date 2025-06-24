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

    def test_splittest_Having_a_TextNode_that_is_missing_markup_should_return_nothing_as_there_is_no_match(self):
        test_text_node = TextNode("", TextType.TEXT)
        result = split_nodes_delimiter([test_text_node], "'", TextType.CODE)
        
        self.assertEqual(len(result), 1, "nothing to split from the original, but should at least get the original back")
        self.assertEqual(result[0], test_text_node, "there is nothing to split here, so result should be unchanged")

    def test_splittest_Having_an_empty_TextNode_with_matching_delimiter_then_should_return_an_empty_result(self):
        test_text_node = TextNode("''", TextType.TEXT)
        test_text_type = TextType.CODE
        result = split_nodes_delimiter([test_text_node], "'", test_text_type)
        
        self.assertEqual(len(result), 0, "there is no text to return")        

    def test_splittest_Having_a_simple_TextNode_with_matching_delimiter_should_return_a_TextNode_matching_delimiter_type(self):
        test_text = "a"
        test_text_node = TextNode(f"'{test_text}'", TextType.TEXT)
        test_text_type = TextType.CODE
        result = split_nodes_delimiter([test_text_node], "'", TextType.CODE)
        
        self.assertEqual(len(result), 1, "delimiter surrounds empty text so only needs a single node to hold this data")
        self.assertEqual(result[0].text_type, test_text_type, "we should have a match on the test type this time, so result should match")
        self.assertEqual(result[0].text, "a", "markup should have been removed, leaving only empty text")

    def test_splittest_Having_simple_text_with_following_markup_TextNode_should_return_TextNodes_mapped_to_the_correct_type(self):
        test_basic_text = "start"
        test_code_text = "finish"
        test_text_node = TextNode(f"{test_basic_text}'{test_code_text}'", TextType.TEXT)
        test_text_type = TextType.CODE
        result = split_nodes_delimiter([test_text_node], "'", test_text_type)
        
        self.assertEqual(len(result), 2, "we now have standard text ending with some markup")
        
        self.assertEqual(result[0].text_type, TextType.TEXT, "source text begins with plain text no markup")
        self.assertEqual(result[0].text, test_basic_text, "first node should contain the basic text")

        self.assertEqual(result[1].text_type, test_text_type, "our test ends the test text")
        self.assertEqual(result[1].text, test_code_text, "second node should contain the converted text")

    def test_splittest_Having_simple_text_starting_with_markup_TextNode_should_return_TextNodes_mapped_to_the_correct_type(self):
        test_basic_text = "start"
        test_code_text = "finish"
        test_text_node = TextNode(f"'{test_code_text}'{test_basic_text}", TextType.TEXT)
        test_text_type = TextType.CODE
        result = split_nodes_delimiter([test_text_node], "'", test_text_type)
        
        self.assertEqual(len(result), 2, "we now have standard text ending with some markup")
        
        self.assertEqual(result[0].text_type, test_text_type, "markup is at the start of the test text")
        self.assertEqual(result[0].text, test_code_text, "first node should contain the converted text")

        self.assertEqual(result[1].text_type, TextType.TEXT, "source text begins with plain text no markup")
        self.assertEqual(result[1].text, test_basic_text, "second node should contain the basic text")

    def test_splittest_Having_simple_text_with_markup_embedded_TextNode_should_return_TextNodes_mapped_to_the_correct_type(self):
        test_basic_text = "start"        
        test_code_text = "middle"
        test_end_text = "end"
        test_text_node = TextNode(f"{test_basic_text}'{test_code_text}'{test_end_text}", TextType.TEXT)
        test_text_type = TextType.CODE
        result = split_nodes_delimiter([test_text_node], "'", test_text_type)
        
        self.assertEqual(len(result), 3, "we now have some markup embedded in the middle")
        
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[0].text, test_basic_text)

        self.assertEqual(result[1].text_type, test_text_type, "markup is in the middle")
        self.assertEqual(result[1].text, test_code_text, "second node should therefore contain the converted text")

        self.assertEqual(result[2].text_type, TextType.TEXT)
        self.assertEqual(result[2].text, test_end_text)

    

        


if __name__ == "__main__":
    unittest.main()