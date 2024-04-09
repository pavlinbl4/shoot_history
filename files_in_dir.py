from loguru import logger
from pathlib import Path


def get_all_files(directory_path):
    return [str(p) for p in Path(directory_path).glob("**/*")]


if __name__ == '__main__':


    # directory_path = '/Volumes/big4photo-4/selenium_downloads/keyword_["пешеход"]'
    # print(get_all_files(directory_path))

    directory_path = "/Volumes/big4photo-4/selenium_downloads/keyword_['пешеход']"
    all_files = [str(p) for p in Path(directory_path).glob("**/*")]
    print(all_files)

