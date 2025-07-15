import re


def get_file_extension(path_to_file: str) -> str:
    # re_pattern = r'(?<=\.)[1A-Za-z_]{3,8}'  # work correctly with only one dot in filename
    re_pattern = r'(?<=\.)[^.]+$'
    extension = re.findall(re_pattern, path_to_file)[0]
    return extension  # string with file extension


def get_file_name_no_extension(file_name: str):
    rg_pattern = r'[^.]+(?=\.)'
    # didn't work with hidden files
    file_name_no_extension = re.findall(rg_pattern, file_name)
    if len(file_name_no_extension) != 0:
        return file_name_no_extension[0]



