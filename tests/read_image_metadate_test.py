from unittest import TestCase, main

from shoot_history.exif_job import read_image_metadate


class ReadImageMeyadata(TestCase):
    def test_read_image_metadate(self):
        self.assertEqual(read_image_metadate('tests/test_files/20231214EPAV9435.jpg'), 'xxx')


if __name__ == '__main__':
    main()
    print(read_image_metadate('tests/test_files/20231214EPAV9435.jpg'))
