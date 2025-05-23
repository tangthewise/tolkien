from textnode import *

def main():
    my_text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(my_text_node)

main()