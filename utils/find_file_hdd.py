import logging
import os

from utils.regex_tools import get_file_extension, get_file_name_no_extension


def find_no_ext(file_name_no_extension: str, path: str):  # this will match a file_name
    result = []
    for root, files in os.walk(path):
        for file in [elem for elem in files if elem.split('.')[-1].lower() in ('dng', 'nef', 'orf', 'jpg', 'jpeg')]:
            if get_file_name_no_extension(file) == file_name_no_extension:
                result.append(os.path.join(root, file))
    return result  # возвращает список с путем к оригинальному файлу


