from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:

            if node.text.count(delimiter) % 2 != 0:
                raise ValueError(f"Delimiter '{delimiter}' not found as a matching pair")

            parts = node.text.split(delimiter)
            for i, part in enumerate(parts):
                if part == "":
                    continue
                node_type = text_type if i % 2 != 0 else TextType.TEXT
                new_nodes.append(TextNode(part, node_type, node.url))
        else:
            new_nodes.append(node)
    return new_nodes


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    
    for node in old_nodes:        
            images = extract_markdown_images(node.text)
            if images:
                for alt_text, url in images:
                    new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            else:
                new_nodes.append(node)
        
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    
    for node in old_nodes:        
            links = extract_markdown_links(node.text)
            if links:
                for link_text, url in links:
                    new_nodes.append(TextNode(link_text, TextType.LINK, url))
            else:
                new_nodes.append(node)
        
    return new_nodes



def extract_markdown_images(text: str) -> list[str]:
    import re

    image_regex = r'!\[([^\[\]]*)\]\(([^\(\)]*)\)'

    images = re.findall(image_regex, text)    

    return images


def extract_markdown_links(text: str) -> list[str]:
    import re

    link_regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"

    links = re.findall(link_regex, text)    

    return links