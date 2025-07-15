import exiftool
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
