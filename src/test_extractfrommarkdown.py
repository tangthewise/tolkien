import unittest


class TestExtractFromMarkdown(unittest.TestCase):
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

