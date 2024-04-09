from unittest import TestCase, main

from shoot_history.exif_job import read_image_metadate

TEST_JPEG = "/Users/evgenii/PycharmProjects/shoot_history/tests/test_files/20231214EPAV9435.jpg"


class ReadImageMetadata(TestCase):
    def test_read_image_metadate(self):
        self.assertIsInstance(read_image_metadate(TEST_JPEG), dict)
        self.assertEqual(read_image_metadate(TEST_JPEG)['Composite:LensID'], 'OLYMPUS M.7-14mm F2.8')


if __name__ == '__main__':
    main()
