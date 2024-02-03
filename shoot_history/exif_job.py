import exiftool
from icecream import ic
from kp_selenium_tools.regex_tools import modify_caption


def change_color_class(file, image_title, color):
    with exiftool.ExifToolHelper() as et:
        et.set_tags(
            [file],
            tags={"XMP:Title": image_title,
                  "IPTC:ObjectName": image_title,
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
    test_ol_image = '/Users/evgeniy/Pictures/2024/01_January/20240113_Пожар на складе Wildberries/20240113PEV_2551.NEF'
    # write_data_to_photo_iptc_tools(test_ol_image)
    # change_color_class(test_ol_image, 'exiftool', "Red")
    ic(read_image_metadate(test_ol_image))

