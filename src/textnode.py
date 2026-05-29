from leafnode import LeafNode
from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = None): # type: ignore
        self.text = text
        self.text_type = text_type
        self.url = url
 
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return NotImplemented
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __str__(self): #Human-readable string representation of the TextNode
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def __repr__(self): #Detailed string representation of the TextNode, useful for debugging
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
        
        if text_node.text_type == TextType.TEXT:
            return LeafNode(None, text_node.text)

        elif text_node.text_type == TextType.BOLD:
            return LeafNode("b", text_node.text)

        elif text_node.text_type == TextType.ITALIC:
            return LeafNode("i", text_node.text)

        elif text_node.text_type == TextType.CODE:
            return LeafNode("code", text_node.text)

        elif text_node.text_type == TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url} )

        elif text_node.text_type == TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})            

        else:
            raise ValueError(f"Unsupported text type: {text_node.text_type}")