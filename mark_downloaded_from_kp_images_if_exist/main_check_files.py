from kp_selenium_tools.authorization import AuthorizationHandler
from mark_downloaded_from_kp_images_if_exist.check_image_on_site import find_image
from shoot_history.exif_job import change_color_class, clear_image_metadata_from_kp_info
from shoot_history.find_file_hdd import action_with_image_files_in_directory
from loguru import logger
from pathlib import Path
import time
from random import randint
logger.disable('__main__')


def example_function_to_work_with_files(path):

    # logger.info(path)
    photo_id = Path(path).stem[:-3]
    logger.info(photo_id)
    time.sleep(randint(1,15))
    # logger.info(find_image(photo_id))
    if find_image(photo_id):
        change_color_class(path, photo_id, color='Red')
        logger.info(f'set red color to image {photo_id}')
    else:
        clear_image_metadata_from_kp_info(path)


def main():
    # check downloaded folder
    action_with_image_files_in_directory('/Volumes/big4photo-4/selenium_downloads', example_function_to_work_with_files)


if __name__ == '__main__':
    main()
