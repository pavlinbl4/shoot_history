from unittest import TestCase, main
from shoot_history.scrap_html import check_original_file_name


class TestCheckOriginalFileName(TestCase):
    def test_check_original_file_name(self):
        # Test case: the filename starts with "E"
        self.assertEqual(check_original_file_name("Efile.txt", "2024-03-13"), "2024-03-13Efile.txt")

        # Test case: the filename starts with "P"
        self.assertEqual(check_original_file_name("Pfile.txt", "2024-03-13"), "2024-03-13Pfile.txt")

        # Test case: the filename does not start with "E" or "P"
        self.assertEqual(check_original_file_name("file.txt", "2024-03-13"), "file.txt")

        # Test case: the filename starts with lower case "e" or "p"
        self.assertEqual(check_original_file_name("efile.txt", "2024-03-13"), "efile.txt")
        self.assertEqual(check_original_file_name("pfile.txt", "2024-03-13"), "pfile.txt")


if __name__ == "__main__":
   main()
