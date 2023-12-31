import os

from kp_selenium_tools.regex_tools import get_file_extension, get_file_name_no_extension


def find_no_ext(file_name_no_extension: str, path: str):  # this will match a file_name
    result = []
    for root, dirs, files in os.walk(path):
        for file in [elem for elem in files if  elem.split('.')[-1].lower() in ('dng',  'nef', 'orf', 'jpg', 'jpeg')]:
            if get_file_name_no_extension(file) == file_name_no_extension:
                result.append(os.path.join(root, file))
    return result  # возвращает список с путем к оригинальному файлу


def action_with_image_files_in_directory(path, action_with_files):
    for root, dirs, files in os.walk(path):
        for file in files:
            if get_file_extension(file).lower() in ('jpg', 'jpeg', 'ORF', 'DNG', 'dng', 'NEF', 'nef', 'orf'):
                # you can add any function to work with file
                action_with_files(f"{root}/{file}")

                print(f"{root}/{file}")


if __name__ == '__main__':
    # action_with_image_files_in_directory('/Volumes/big4photo-4/EDITED_JPEG_ARCHIV/Downloaded_from_fotoagency/Deleted_shoots')

    assert type(find_no_ext('20230321PEV_9941-Edit', '/Volumes/big4photo-4/2023_main_archiv')) == list
    assert '20230321PEV_9941-Edit' in find_no_ext('20230321PEV_9941-Edit', '/Volumes/big4photo-4/2023_main_archiv')[0]

    assert len(find_no_ext('20231006EPAV2451', '/Users/evgeniy/Pictures/2023/20231006_Асфальто-бетонный завод')) == 1
