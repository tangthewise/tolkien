import re
from enum import Enum

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode
from parentnode import ParentNode


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def text_to_textnodes(text: str) -> list[TextNode]:
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    return [block.strip() for block in blocks if block.strip()]


def block_to_block_type(block: str) -> BlockType:
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING

    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    lines = block.split("\n")

    if all(re.match(r"^> ?", line) for line in lines):
        return BlockType.QUOTE

    if all(re.match(r"^- ", line) for line in lines):
        return BlockType.UNORDERED_LIST

    if all(re.match(r"^\d+\. ", line) for line in lines):
        for index, line in enumerate(lines, start=1):
            if not re.match(rf"^{index}\. ", line):
                break
        else:
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

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
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        images = list(re.finditer(r'!\[([^\[\]]*)\]\(([^\(\)]*)\)', text))
        if not images:
            new_nodes.append(node)
            continue

        start = 0
        for image in images:
            if image.start() > start:
                new_nodes.append(TextNode(text[start:image.start()], TextType.TEXT))
            new_nodes.append(TextNode(image.group(1), TextType.IMAGE, image.group(2)))
            start = image.end()

        if start < len(text):
            new_nodes.append(TextNode(text[start:], TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        links = list(re.finditer(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text))
        if not links:
            new_nodes.append(node)
            continue

        start = 0
        for link in links:
            if link.start() > start:
                new_nodes.append(TextNode(text[start:link.start()], TextType.TEXT))
            new_nodes.append(TextNode(link.group(1), TextType.LINK, link.group(2)))
            start = link.end()

        if start < len(text):
            new_nodes.append(TextNode(text[start:], TextType.TEXT))

    return new_nodes



def extract_markdown_images(text: str) -> list[str]:
    image_regex = r'!\[([^\[\]]*)\]\(([^\(\)]*)\)'

    images = re.findall(image_regex, text)

    return images


def extract_markdown_links(text: str) -> list[str]:
    link_regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"

    links = re.findall(link_regex, text)

    return links


def text_to_children(text: str) -> list[HTMLNode]:
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(text_node) for text_node in text_nodes]


def paragraph_to_html_node(block: str) -> HTMLNode:
    text = " ".join(block.split("\n"))
    return ParentNode("p", text_to_children(text))


def heading_to_html_node(block: str) -> HTMLNode:
    match = re.match(r"^(#{1,6}) ", block)
    level = len(match.group(1))
    text = block[level + 1:]
    return ParentNode(f"h{level}", text_to_children(text))


def code_to_html_node(block: str) -> HTMLNode:
    text = block[3:-3]
    if text.startswith("\n"):
        text = text[1:]
    code_leaf = text_node_to_html_node(TextNode(text, TextType.TEXT))
    code_node = ParentNode("code", [code_leaf])
    return ParentNode("pre", [code_node])


def quote_to_html_node(block: str) -> HTMLNode:
    lines = [re.sub(r"^> ?", "", line) for line in block.split("\n")]
    text = " ".join(line for line in lines if line.strip())
    return ParentNode("blockquote", text_to_children(text))


def unordered_list_to_html_node(block: str) -> HTMLNode:
    items = []
    for line in block.split("\n"):
        text = line[2:]
        items.append(ParentNode("li", text_to_children(text)))
    return ParentNode("ul", items)


def ordered_list_to_html_node(block: str) -> HTMLNode:
    items = []
    for line in block.split("\n"):
        text = re.sub(r"^\d+\. ", "", line)
        items.append(ParentNode("li", text_to_children(text)))
    return ParentNode("ol", items)


def block_to_html_node(block: str) -> HTMLNode:
    block_type = block_to_block_type(block)

    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    if block_type == BlockType.UNORDERED_LIST:
        return unordered_list_to_html_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return ordered_list_to_html_node(block)

    raise ValueError(f"Unsupported block type: {block_type}")


def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    children = [block_to_html_node(block) for block in blocks]
    return ParentNode("div", children)