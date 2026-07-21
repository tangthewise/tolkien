import unittest


class TestExtractFromMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        from split_nodes import markdown_to_blocks

        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_strips_and_removes_empty_blocks(self):
        from split_nodes import markdown_to_blocks

        md = "\n\n  First block  \n\n\nSecond block\n\n   \n\nThird block   \n\n"

        self.assertEqual(
            markdown_to_blocks(md),
            ["First block", "Second block", "Third block"],
        )

    def test_extract_images_from_markdown(self):
        from split_nodes import extract_markdown_images
        
        markdown = """
        # Sample Markdown
        
        This is a sample markdown document with images.
        
        ![Image 1](https://example.com/image1.png)
        
        Some text in between.
        
        ![Image 2](https://example.com/image2.jpg)
        
        End of the document.
        """
        
        expected_images = [
            ("Image 1", "https://example.com/image1.png"),
            ("Image 2", "https://example.com/image2.jpg")
        ]
        
        extracted_images = extract_markdown_images(markdown)
        
        self.assertEqual(extracted_images, expected_images)

    def test_extract_links_from_markdown(self):
        from split_nodes import extract_markdown_links
        
        markdown = """
        # Sample Markdown
        
        This is a sample markdown document with links.
        
        [Google](https://www.google.com)
        
        Some text in between.
        
        [OpenAI](https://www.openai.com)
        
        End of the document.
        """
        
        expected_links = [
            ("Google", "https://www.google.com"),
            ("OpenAI", "https://www.openai.com")
        ]
        
        extracted_links = extract_markdown_links(markdown)
        
        self.assertEqual(extracted_links, expected_links)

