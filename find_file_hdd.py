import logging
import os

from kp_selenium_tools.regex_tools import get_file_extension, get_file_name_no_extension


def find_no_ext(file_name_no_extension: str, path: str):  # this will match a file_name
    result = []
    for root, dirs, files in os.walk(path):
        for file in [elem for elem in files if elem.split('.')[-1].lower() in ('dng', 'nef', 'orf', 'jpg', 'jpeg')]:
            if get_file_name_no_extension(file) == file_name_no_extension:
                result.append(os.path.join(root, file))
    return result  # возвращает список с путем к оригинальному файлу


# function to find all images and send them to function
def action_with_image_files_in_directory(path: str, process_file_function):
    # Устанавливаем логгер
    logger = logging.getLogger(__name__)

    # Множество допустимых расширений изображений
    valid_extensions = {'jpg', 'jpeg', 'orf', 'dng', 'nef'}

    for root, _, files in os.walk(path):  # игнорируем список директорий (dirs) через `_`
        logger.info(f"Scanning directory: {root}")

        for file in files:
            if get_file_extension(file).lower() in valid_extensions:
                # you can add any function to work with file
                full_path = os.path.join(root, file)
                process_file_function(full_path)
