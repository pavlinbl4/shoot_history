from bs4 import BeautifulSoup
from colorama import Fore
from loguru import logger

from exif_job import change_color_class
from find_file_hdd import find_no_ext
from kp_selenium_tools.save_info_in_csv import write_lost_files_info


logger.disable('__main__')


def find_file_on_hdd(uploaded_images_dict, path_to_images_folder, photo_id, image_caption):
    original_file_name = uploaded_images_dict[photo_id][0]
    way_to_file = find_no_ext(original_file_name, path_to_images_folder)
    # if file wasn't found
    if len(way_to_file) > 0:
        change_color_class(way_to_file[0], photo_id, image_caption, color='Red')

    else:
        print(f"{Fore.RED} I don't find {original_file_name} in {path_to_images_folder}{Fore.RESET}")
        write_lost_files_info(original_file_name, photo_id)


def scrap_html(page_link: str):
    soup = BeautifulSoup(page_link, 'lxml')
    trs = soup.find('table', id='ProcessingGrid').find('tbody').find_all('tr')
    # logger.info(len(trs))
    trs_pub = soup.find('table', id='HistoryLogGrid').find('tbody').find_all('tr')

    # получаю дату передачи съемки из последней строки таблицы
    komm_dates = soup.find_all('tr', class_="row-alternating")
    komm_date = komm_dates[-1].find('td', class_="date-col").text[:10].split(
        '.')

    my_date_format: str = komm_date[2] + komm_date[1] + komm_date[0]
    print(f'{my_date_format = }')
    return my_date_format, trs, trs_pub


# add information to dict about added images - 'KSP_018323_00039': ['20241210PEV_1903', 'ADDED']
def find_added_to_kp_images(trs_pub, uploaded_images_dict, my_date_format, path):
    original_file_name = None
    photo_id = None

    # список добавленных в архив фото
    added_photo_id_list = []
    for i in range(len(trs_pub)):
        xxx = trs_pub[i].find(class_="user-col").find_next('td').text
        if 'Добавлен:' in xxx:
            photo_id = trs_pub[i].find(class_="user-col").find_next('td').text[10:-2]  # id added image
            # logger.info(f'{photo_id = }')

            # проверяю - файл переименован по моим правилам или отправлен с камеры
            original_file_name = check_original_file_name(uploaded_images_dict[photo_id][0],
                                                          my_date_format)  # file name no extension
            print(f"for file {photo_id} original filename is  {original_file_name}")
            uploaded_images_dict[photo_id].append("ADDED")
            added_photo_id_list.append(photo_id)
    logger.info(f'{added_photo_id_list = }')
    logger.info(f'Добавлено в архив {len(added_photo_id_list)} снимков')



    return added_photo_id_list


def check_original_file_name(original_file_name: str,
                             my_date_format: str) -> str:
    # проверяю, был ли файл переименован по моим правилам или отправлен сразу с камеры
    if original_file_name.startswith("E") or original_file_name.startswith("P"):
        print(
            f'{Fore.MAGENTA}{original_file_name} was uploaded from camera and '
            f'it name on hdd must be {my_date_format + original_file_name}{Fore.RESET}')
        original_file_name = my_date_format + original_file_name
    return original_file_name


def find_all_uploaded_images(page_link: str, path: str):
    # get data from html
    my_date_format, trs, trs_pub = scrap_html(page_link)

    # create dict with KP and uploaded filenames dict {photo_id:[uploaded_file_name]}
    uploaded_images_dict = {}
    for i in range(1, len(trs)):
        uploaded_images_dict[trs[i].find('td').find_next('td').text[:-6]] = [
            trs[i].find('td').text[:-4]]
    # logger.info(F'{uploaded_images_dict = }')
    logger.info(F'всего загружено - {len(uploaded_images_dict) = } снимков')

    # add added images to dict и получаю список id опубликованных файлов
    added_photo_id_list = find_added_to_kp_images(trs_pub, uploaded_images_dict, my_date_format, path)

    return added_photo_id_list, uploaded_images_dict  # возвращает словарь переименованных снимков -  {photo_id:[uploaded_file_name]}


if __name__ == '__main__':
    with open('/Users/evgeniy/Documents/Kommersant/source_page.html', 'r') as html_file:
        page_link_ex = html_file.read()

    print(find_all_uploaded_images(page_link=page_link_ex,
                                   path='/Users/evgeniy/Pictures/2024'))
