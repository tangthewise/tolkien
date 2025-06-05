import unittest

from leafnode import LEAFNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_parent_missing_tag_should_be_invalid(self):
        node = ParentNode(None, None)
        
        with self.assertRaises(ValueError):
            node.to_html()
            
            
    def test_parent_missing_children_should_be_invalid(self):
        node = ParentNode("p", None)
        
        with self.assertRaises(ValueError):
            node.to_html()  

    def test_parent_with_empty_children_should_be_invalid(self):
        node = ParentNode("p", {})
        
        with self.assertRaises(ValueError):
            node.to_html()  

    def test_basic_parent_with_single_child_should_be_valid(self):
        test_tag = "p"
        test_child_tag = "b"
        test_child_value = "in bold"

        child_node = LEAFNode(test_child_value, test_child_tag)

        node = ParentNode(test_tag, [child_node])

        Expected_HTML = f"<{test_tag}>{child_node.to_html()}</{test_tag}>"
        
        self.assertEqual(Expected_HTML, node.to_html())

    def test_typical_parent_with_several_children_should_be_valid(self):
        node = ParentNode(
            "p",
            [
                LEAFNode("Bold text", "b"),
                LEAFNode("Normal text", None),
                LEAFNode("italic text", "i"),
                LEAFNode("Normal text", None),
            ],
            )
        expected_result = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"

        self.assertEqual(expected_result, node.to_html())
    
    

if __name__ == "__main__":
    unittest.main()