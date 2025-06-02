import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_empty_props(self):
        node = HTMLNode()
        
        propsString = node.props_to_html()

        self.assertEqual(f"{propsString}", "")

    def test_simple_property_should_be_rendered_correctly(self):
        property_name = "property"
        property_value = "myproperty"
        Expected_Output = f" {property_name}=\"{property_value}\""

        node = HTMLNode(props={property_name: property_value})
        
        propsString = node.props_to_html()
        
        self.assertEqual(f"{propsString}", Expected_Output)

    def test_multiple_properties_should_be_rendered_correctly(self):
        property_name1 = "property1"
        property_value1 = "myproperty1"
        property_name2 = "property2"
        property_value2 = "myproperty2"
        Expected_Output = f" {property_name1}=\"{property_value1}\" {property_name2}=\"{property_value2}\""

        node = HTMLNode(props={property_name1: property_value1, property_name2: property_value2})        
        propsString = node.props_to_html()

        
        self.assertEqual(f"{propsString}", Expected_Output)


if __name__ == "__main__":
    unittest.main()