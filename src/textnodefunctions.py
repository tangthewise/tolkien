import re
from textnode import TextType, TextNode
from leafnode import LEAFNode

def text_node_to_html_node(text_node):
        result = LEAFNode(text_node.text)

        match text_node.text_type:
            case TextType.TEXT:
                pass
            case TextType.BOLD:
                result.tag = "b"
            case TextType.ITALIC:
                result.tag = "i"
            case TextType.CODE:
                result.tag = "code"
            case TextType.LINK:
                result.tag = "a"
                properties = { "href":text_node.url }
                result.props = properties 
            case TextType.IMAGE:
                result.tag = "img"
                result.value = ""
                result.props = { "src": text_node.url, "alt": text_node.text }
            case _:
                raise Exception(f"Unknown TextType: {text_node.text_type}")

        return result

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def xtract_markdown_images(text):        
            image_regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
            return extract_markdown(image_regex, text)

def xtract_markdown_links(text):        
            link_regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
            return extract_markdown(link_regex, text)

def extract_markdown(regex, text):
        result = list()
        
        if text != None and len(text) > 0:           
            
            result.extend(re.findall(regex, text))            
            
            

        return result
    
