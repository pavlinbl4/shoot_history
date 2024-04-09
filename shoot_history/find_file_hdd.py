import os
from kp_selenium_tools.regex_tools import get_file_extension, get_file_name_no_extension
from loguru import logger


def find_no_ext(file_name_no_extension: str, path: str):  # this will match a file_name
    result = []
    for root, dirs, files in os.walk(path):
        for file in [elem for elem in files if elem.split('.')[-1].lower() in ('dng', 'nef', 'orf', 'jpg', 'jpeg')]:
            if get_file_name_no_extension(file) == file_name_no_extension:
                result.append(os.path.join(root, file))
    return result  # возвращает список с путем к оригинальному файлу


def example_function_to_work_with_files(path):
    print(path)


# function to find all images and send them to function
def action_with_image_files_in_directory(path: str, function_to_work_with_files):
    # logger.info(path)
    for root, dirs, files in os.walk(path):
        logger.info(root)
        logger.info(dirs)
        for file in files:
            if get_file_extension(file).lower() in ('jpg', 'jpeg', 'ORF', 'DNG', 'dng', 'NEF', 'nef', 'orf'):
                # you can add any function to work with file
                function_to_work_with_files(f"{root}/{file}")




if __name__ == '__main__':
    # action_with_image_files_in_directory('/Volumes/big4photo-4/EDITED_JPEG_ARCHIV/Downloaded_from_fotoagency/Deleted_shoots')

    # assert type(find_no_ext('20230321PEV_9941-Edit', '/Volumes/big4photo-4/2023_main_archiv')) == list
    # assert '20230321PEV_9941-Edit' in find_no_ext('20230321PEV_9941-Edit', '/Volumes/big4photo-4/2023_main_archiv')[0]

    # assert len(find_no_ext('20231006EPAV2451', '/Users/evgeniy/Pictures/2023/20231006_Асфальто-бетонный завод')) == 1

    action_with_image_files_in_directory("/Volumes/big4photo-4/selenium_downloads/keyword_['пешеход']",
                                         example_function_to_work_with_files)
    # print(find_no_ext('jpg','/Volumes/big4photo-4/selenium_downloads/keyword_манекен'))
