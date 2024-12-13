from bs4 import BeautifulSoup

from colorama import Fore
from kp_selenium_tools.save_info_in_csv import write_lost_files_info
from shoot_history.exif_job import change_color_class
from shoot_history.find_file_hdd import find_no_ext
from loguru import logger

# logger.disable('__main__')


def find_file_on_hdd(original_file_name, path, photo_id):
    way_to_file = find_no_ext(original_file_name, path)
    # if file wasn't found
    if len(way_to_file) > 0:
        change_color_class(way_to_file[0], photo_id, color='Red')
    else:
        print(f"{Fore.RED} I don't find {original_file_name} in {path}{Fore.RESET}")
        write_lost_files_info(original_file_name, photo_id)


def scrap_html(page_link: str):
    soup = BeautifulSoup(page_link, 'lxml')
    trs = soup.find('table', id='ProcessingGrid').find('tbody').find_all('tr')
    logger.info(len(trs))
    trs_pub = soup.find('table', id='HistoryLogGrid').find('tbody').find_all('tr')


    # получаю дату передачи съемки из последней строки таблицы
    komm_dates = soup.find_all('tr', class_="row-alternating")
    komm_date = komm_dates[-1].find('td', class_="date-col").text[:10].split(
        '.')



    my_date_format: str = komm_date[2] + komm_date[1] + komm_date[0]
    print(f'{my_date_format = }')
    return my_date_format, trs, trs_pub


# add information to dict about added images
def find_added_to_kp_images(trs_pub, file_renames, my_date_format, path):
    original_file_name = None
    photo_id = None
    for i in range(len(trs_pub)):
        xxx = trs_pub[i].find(class_="user-col").find_next('td').text
        if 'Добавлен:' in xxx:
            photo_id = trs_pub[i].find(class_="user-col").find_next('td').text[10:-2]  # id added image
            logger.info(f'{photo_id = }')
            original_file_name = check_original_file_name(file_renames[photo_id][0],
                                                          my_date_format)  # file name no extension
            print(f"for file {photo_id} original filename is  {original_file_name}")
            file_renames[photo_id].append("ADDED")

            find_file_on_hdd(original_file_name, path, photo_id)

    return original_file_name, photo_id


def check_original_file_name(original_file_name: str,
                             my_date_format: str) -> str:
    # проверяю, был ли файл переименован по моим правилам или отправлен сразу с камеры
    if original_file_name.startswith("E") or original_file_name.startswith("P"):
        print(
            f'{Fore.MAGENTA}{original_file_name} was uploaded from camera and '
            f'it name on hdd must be {my_date_format + original_file_name}{Fore.RESET}')
        original_file_name = my_date_format + original_file_name
    return original_file_name


def main_parse_page(page_link: str, path: str):
    # get data from html
    my_date_format, trs, trs_pub = scrap_html(page_link)

    # create dict with KP and uploaded filenames dict {kommers)file_name:[my_file_name]}
    file_renames = {}
    for i in range(1, len(trs)):
        file_renames[trs[i].find('td').find_next('td').text[:-6]] = [
            trs[i].find('td').text[:-4]]
    logger.info(F'{file_renames = }')

    # add added images to dict
    original_file_name, photo_id = find_added_to_kp_images(trs_pub, file_renames, my_date_format, path)

    # function to find file on HDD, path - to directory
    # way_to_file = find_no_ext(original_file_name, path)
    # # if file wasn't found
    # if len(way_to_file) > 0:
    #     change_color_class(way_to_file[0], photo_id, color='Red')
    # else:
    #     print(f"{Fore.RED} I don't find {original_file_name} in {path}{Fore.RESET}")
    #     write_lost_files_info(original_file_name, photo_id)
    return file_renames  # возвращает словарь переименованных снимков


if __name__ == '__main__':
    with open('/Volumes/big4photo/_PYTHON/shoot_history/tests/test_files/test_file.html', 'r') as html_file:
        page_link_ex = html_file.read()

    print(main_parse_page(page_link=page_link_ex,
                          path='tests/test_files/20211201PEV_2795-Edit.JPG'))
