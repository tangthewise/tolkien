import unittest

from textnode import TextNode, TextType
from textnodefunctions import xtract_markdown_links


class TestXTractLinkMarkdownFunction(unittest.TestCase):    

    def test_initial_empty_result(self):

        result = xtract_markdown_links("")

        self.assertEqual(len(result), 0, "the text is empty so nothing to return")

    def test_text_that_is_missing_image_detail_should_return_empty(self):

        result = xtract_markdown_links("here is some non markup text")

        self.assertEqual(len(result), 0, "the text has no image markup so nothing to return")


    def test_text_that_has_bad_image_markup_should_return_empty(self):

        text = " dev](https://www.boot.dev)"

        result = xtract_markdown_links(text)

        self.assertEqual(len(result), 0, "the text has no valid link markup so nothing to return")

    
    def test_text_that_has_single_link_markup_should_return_1_tuple_with_correct_detail(self):

        test_alt_text = "to boot dev"
        test_html_url = "https://www.boot.dev"        
        test_markup = f"[{test_alt_text}]({test_html_url})"

        result = xtract_markdown_links(test_markup)

        self.assertEqual(len(result), 1, "the text contains a single link, so the result should contain a single tuple")

        extracted_image = result[0]
        print(extracted_image)
        self.assertEqual(extracted_image[0], test_alt_text)
        self.assertEqual(extracted_image[1], test_html_url)


    def test_text_that_has_multiple_links_should_return_multiple_tuples_with_correct_detail(self):

        test_alt_text = "to boot dev"
        test_html_url = "https://www.boot.dev"        
        test2_alt_text = "to youtube"
        test2_url = "https://www.youtube.com/@bootdotdev"
        text = f"This is text with a link [{test_alt_text}]({test_html_url}) and [{test2_alt_text}]({test2_url})"

        result = xtract_markdown_links(text)

        self.assertEqual(len(result), 2, "the text contains multiple images, so the result should contain those images in the list of tuples")

        extracted_image_1 = result[0]        
        self.assertEqual(extracted_image_1[0], test_alt_text)
        self.assertEqual(extracted_image_1[1], test_html_url)

        extracted_image_2 = result[1]        
        self.assertEqual(extracted_image_2[0], test2_alt_text)
        self.assertEqual(extracted_image_2[1], test2_url)

    