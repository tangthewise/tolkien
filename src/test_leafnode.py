import unittest

from leafnode import LEAFNode


class TestLeafNode(unittest.TestCase):
    def test_emptynode_should_be_invalid_html(self):
        node = LEAFNode(None)
        
        with self.assertRaises(ValueError):
            node.to_html()

    def test_text_only_node_should_return_raw_text(self):
        Expected_Result = "here is my node"

        node = LEAFNode(Expected_Result)

        self.assertEqual(Expected_Result, node.to_html())
    
    def test_including_tag_should_return_tag_formatted(self):
        test_tag = "p"
        test_value = "my own paragraph"        
        Expected_Result = f"<{test_tag}>{test_value}</{test_tag}>"
        node = LEAFNode(test_value, test_tag)

        self.assertEqual(Expected_Result, node.to_html())

    def test_including_tag_with_properties_should_return_tag_formatted_ccrectly(self):
        test_tag = "p"
        test_value = "my own paragraph"        
        test_property = "id"
        test_property_value = "myid"
        test_properties = {test_property:test_property_value}
        Expected_Result = f"<{test_tag} {test_property}=\"{test_property_value}\">{test_value}</{test_tag}>"
        node = LEAFNode(test_value, test_tag, test_properties)

        self.assertEqual(Expected_Result, node.to_html())


    

if __name__ == "__main__":
    unittest.main()