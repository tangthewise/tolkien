from textnode import TextNode, TextType


def main():
    new_node = TextNode("My text node", TextType.LINK, "http://example.com")
    print(new_node)


main()