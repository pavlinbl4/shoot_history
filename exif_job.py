import exiftool
from icecream import ic
from kp_selenium_tools.regex_tools import modify_caption
from loguru import logger


def change_color_class(path_to_file, photo_id, image_caption, color):
    logger.info(f'{path_to_file = }')
    logger.info(f'{photo_id = }')
    logger.info(f'{image_caption = }')
    with exiftool.ExifToolHelper() as et:
        et.set_tags(
            [path_to_file],
            tags={"XMP:Title": photo_id,
                  "IPTC:ObjectName": photo_id,
                  'XMP:Description': image_caption,
                  'XMP:Label': color,
                  'XMP:Creator': 'Eugene Pavlenko'},
            params=["-P", "-overwrite_original"]
        )


def write_data_to_photo_iptc_tools(file):
    with exiftool.ExifToolHelper() as et:
        title = "exiftool"
        et.set_tags(
            [file],
            tags={"XMP:Title": title,
                  "IPTC:ObjectName": title,
                  'XMP:Label': "Green",
                  'XMP:Subject': "keywords/exiftool",
                  'XMP:Description': "caption/exiftool",
                  'XMP:Rating': "3",
                  'XMP:Creator': 'Eugene Pavlenko/exiftool'},
            params=["-P", "-overwrite_original"]
        )


def write_edited_tags(xmp_tags):
    with exiftool.ExifToolHelper() as et:
        et.set_tags({xmp_tags['SourceFile']},
                    tags={'XMP:Rights': 'Pavlenko Evgeniy',
                          'XMP:Credit': 'Pavlenko Evgeniy',
                          'XMP:Creator': 'Pavlenko Evgeniy',
                          'XMP:Title': '',
                          'XMP:Label': "Green",
                          'XMP:Description': xmp_tags['XMP:Description'],
                          'IPTC:By-line': 'Pavlenko Evgeniy',
                          'IPTC:Credit': '',
                          'IPTC:CopyrightNotice': 'Pavlenko Evgeniy',
                          'IPTC:Caption-Abstract': xmp_tags['XMP:Description'],
                          'IPTC:ObjectName': '',
                          'Photoshop:SlicesGroupName': ''
                          },
                    params=["-P", "-overwrite_original"])


def read_image_metadate(path_to_image_file):
    with exiftool.ExifToolHelper() as et:
        return et.get_metadata(path_to_image_file)[0]


def clear_image_metadata_from_kp_info(path_to_image_file):
    # read metadata
    image_metadata = read_image_metadate(path_to_image_file)

    # modify caption
    modify_caption(image_metadata)

    # save updates metadata to file
    write_edited_tags(image_metadata)


if __name__ == '__main__':

    # test_ol_image = '/Users/evgeniy/Pictures/test_images/20231006EPAV2225.ORF'
    # test_ol_image = '/Users/evgeniy/PycharmProjects/shoot_history/tests/test_files/20231214EPAV9435.jpg'
    # test_ol_image = '../shoot_history/tests/test_files/20231214EPAV9435.jpg'
    # write_data_to_photo_iptc_tools(test_ol_image)
    change_color_class('/Users/evgeniy/Pictures/2024/12_December/20241211_Ветеринарный университет/20241211EPAV4896.ORF',
                       'exiftool',
                       "10.12.2024 Россия, Санкт-Петербург Участок Широтной магистрали скоростного движения (ШМСД) от Артиллерийского путепровода до Благодатной улицы",
                       'Red')
    # ic(read_image_metadate(test_ol_image))

