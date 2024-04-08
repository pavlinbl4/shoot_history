from unittest import TestCase, main
from shoot_history.scrap_html import main_parse_page, check_original_file_name





class ScrapHtmlTest(TestCase):
    def setUp(self):
        with open('tests/test_files/test_file.html', 'r') as html_file:
            self.page_link = html_file.read()

    def test_output(self):
        self.assertIsInstance(main_parse_page(page_link=self.page_link,
                                              path='test_files/20211201PEV_2795-Edit.JPG'), dict)


if __name__ == '__main__':
    main_parse_page()

    # print(scrap_html(page_link=page_link,
    #                                      path='tests/test_files/20211201PEV_2795-Edit.JPG'))
