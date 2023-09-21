import exiftool

from kp_selenium_tools.regex_tools import modify_caption


def change_color_class(file, image_title, color):
    with exiftool.ExifToolHelper() as et:
        et.set_tags(
            [file],
            tags={"XMP:Title": image_title,
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
    clear_image_metadata_from_kp_info(
        '/Volumes/big4photo-4/EDITED_JPEG_ARCHIV/Downloaded_from_fotoagency/KSP_017775/KSP_017775_00025_1h.jpg')

    m_date = read_image_metadate(
        '/Volumes/big4photo-4/EDITED_JPEG_ARCHIV/Downloaded_from_fotoagency/KSP_017775/KSP_017775_00025_1h.jpg')

    for k, v in m_date.items():
        print(k, v)
