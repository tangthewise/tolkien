import unittest

from split_nodes import split_nodes_delimiter, text_to_textnodes

class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_with_basic_bold_delimiter(self):
        from textnode import TextNode, TextType

        old_nodes = [TextNode("This is a *bold* text", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "*", TextType.BOLD)

        expected_nodes = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]

        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_with_multiple_bold_delimiters(self):
        from textnode import TextNode, TextType

        old_nodes = [TextNode("This is *bold* and this is *also bold*", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "*", TextType.BOLD)

        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and this is ", TextType.TEXT),
            TextNode("also bold", TextType.BOLD)
        ]

        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_with_no_delimiters(self):
        from textnode import TextNode, TextType

        old_nodes = [TextNode("This is a plain text", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "*", TextType.BOLD)

        expected_nodes = [TextNode("This is a plain text", TextType.TEXT)]

        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_With_whole_text_as_bold(self):
        from textnode import TextNode, TextType

        old_nodes = [TextNode("*This is bold text*", TextType.TEXT)]
        
        new_nodes = split_nodes_delimiter(old_nodes, "*", TextType.BOLD)
        
        expected_nodes = [TextNode("This is bold text", TextType.BOLD)]
        
        

    def test_split_nodes_delimiter_no_pairs(self):
        from textnode import TextNode, TextType

        old_nodes = [TextNode("This is a *bold text", TextType.TEXT)]
        
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter(old_nodes, "*", TextType.BOLD)
        
        self.assertIn("Delimiter '*' not found as a matching pair", str(context.exception))

    def test_text_to_textnodes_example(self):
        from textnode import TextNode, TextType

        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        self.assertEqual(text_to_textnodes(text), expected_nodes)



    class TestSplitNodesImage(unittest.TestCase):
        def test_split_nodes_image_with_markdown_image(self):
            from textnode import TextNode, TextType

            old_nodes = [TextNode("This is an image: ![alt text](http://example.com/image.jpg)", TextType.TEXT)]
            new_nodes = split_nodes_image(old_nodes)

            expected_nodes = [
                TextNode("This is an image: ", TextType.TEXT),
                TextNode("alt text", TextType.IMAGE, "http://example.com/image.jpg")
            ]

            self.assertEqual(new_nodes, expected_nodes)


        def test_split_images(self):
            node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",TextType.TEXT,)
            new_nodes = split_nodes_image([node])
            
            self.assertListEqual(
                        [
                            TextNode("This is text with an ", TextType.TEXT),
                            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                            TextNode(" and another ", TextType.TEXT),
                            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                        ],
                        new_nodes
                        )


        def test_split_nodes_image_with_no_markdown_image(self):
            from textnode import TextNode, TextType

            old_nodes = [TextNode("This is a plain text", TextType.TEXT)]
            new_nodes = split_nodes_image(old_nodes)

            expected_nodes = [TextNode("This is a plain text", TextType.TEXT)]

            self.assertEqual(new_nodes, expected_nodes)



        class TestSplitNodesLink(unittest.TestCase):
            def test_split_nodes_link_with_markdown_link(self):
                from textnode import TextNode, TextType

                old_nodes = [TextNode("This is a link: [link text](http://example.com)", TextType.TEXT)]
                new_nodes = split_nodes_link(old_nodes)

                expected_nodes = [
                    TextNode("This is a link: ", TextType.TEXT),
                    TextNode("link text", TextType.LINK, "http://example.com")
                ]

                self.assertEqual(new_nodes, expected_nodes)

            def test_split_nodes_link_with_no_markdown_link(self):
                from textnode import TextNode, TextType

                old_nodes = [TextNode("This is a plain text", TextType.TEXT)]
                new_nodes = split_nodes_link(old_nodes)

                expected_nodes = [TextNode("This is a plain text", TextType.TEXT)]

                self.assertEqual(new_nodes, expected_nodes)