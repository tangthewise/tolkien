import unittest

from textnode import TextNode, TextType
from textnodefunctions import xtract_markdown_images


class TestXTractImageMarkdownFunction(unittest.TestCase):    

    def test_initial_empty_result(self):

        result = xtract_markdown_images("")

        self.assertEqual(len(result), 0, "the text is empty so nothing to return")

    def test_text_that_is_missing_image_detail_should_return_empty(self):

        result = xtract_markdown_images("here is some non image text")

        self.assertEqual(len(result), 0, "the text has no image markup so nothing to return")


    def test_text_that_has_bad_image_markup_should_return_empty(self):

        result = xtract_markdown_images("![(https://i.imgur.c)")

        self.assertEqual(len(result), 0, "the text has no image markup so nothing to return")

    
    def test_text_that_has_single_image_markup_should_return_1_tuple_with_correct_detail(self):

        test_alt_text = "rick roll"
        test_html_url = "https://i.imgur.com/aKaOqIh.gif"
        test_markup = f"![{test_alt_text}]({test_html_url})"

        result = xtract_markdown_images(test_markup)

        self.assertEqual(len(result), 1, "the text contains a single image, so the result should contain a single tuple")

        extracted_image = result[0]
        print(extracted_image)
        self.assertEqual(extracted_image[0], test_alt_text)
        self.assertEqual(extracted_image[1], test_html_url)


    def test_text_that_has_multiple_images_should_return_multiple_tuples_with_correct_detail(self):

        test_alt_text_1 = "rick roll"
        test_html_url_1 = "https://i.imgur.com/aKaOqIh.gif"
        test_alt_text_2 = "obi wan"
        test_html_url_2 = "https://i.imgur.com/fJRm4Vk.jpeg"

        test_markup = f"This is text with a ![{test_alt_text_1}]({test_html_url_1}) and ![{test_alt_text_2}]({test_html_url_2})"

        result = xtract_markdown_images(test_markup)

        self.assertEqual(len(result), 2, "the text contains multiple images, so the result should contain those images in the list of tuples")

        extracted_image_1 = result[0]        
        self.assertEqual(extracted_image_1[0], test_alt_text_1)
        self.assertEqual(extracted_image_1[1], test_html_url_1)

        extracted_image_2 = result[1]        
        self.assertEqual(extracted_image_2[0], test_alt_text_2)
        self.assertEqual(extracted_image_2[1], test_html_url_2)

    