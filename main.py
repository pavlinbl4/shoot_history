from loguru import logger

from utils.authorization import AuthorizationHandler
from utils.check_image_on_site import find_image
from utils.choose_input import clipboard_or_input
from utils.get_shoot_date import get_shoot_date
from utils.make_page_link import make_page_link
from utils.save_page_html import save_html_page, read_html
from utils.scrap_html import find_all_uploaded_images, find_file_on_hdd
from utils.selenium_tools import extract_data_from_page, end_selenium
from utils.tk_tools import select_folder_via_gui


def main():
    # путь к файлу отчета
    # path_to_file = f'{Path().home()}/Documents/Kommersant/shoot_rename/shoot_story.xlsx'

    # номер съемки из буфера обмена или введен в ручную
    shoot_id = clipboard_or_input()
    logger.info(f"{shoot_id = }")

    # путь к папке с изображениями съемки
    # path_to_images_folder = select_folder_via_gui(f'{Path().home()}/Pictures/2024')
    path_to_images_folder = select_folder_via_gui(f'/Volumes/big4photo-2/2025')

    # инициализирую драйвер и авторизуюсь на сайте
    driver = AuthorizationHandler().authorize()
    logger.info("Authorized")

    # генерирую ссылку на нужную страницу
    page_link = make_page_link(shoot_id)
    logger.debug(page_link)

    # open shoot page - without this next link doesn't work
    driver.get(f'https://image.kommersant.ru/photo/archive/search.asp?L=1&code={shoot_id}&ps=100&dt=2&ex=y')

    # открываю эту страницу
    driver.get(page_link)
    # open_page(page_link, driver)

    # получаю данные со страницы истории
    full_history_page_source, inner_id = extract_data_from_page(driver)

    my_date_format = get_shoot_date(driver, inner_id, shoot_id)
    logger.debug(f'my_date_format: {my_date_format}')

    # временно сохраняю страницу
    save_html_page(full_history_page_source)

    # получаю словарь переименованных снимков -  {photo_id:[uploaded_file_name]}
    added_photo_id_list, uploaded_images_dict = find_all_uploaded_images(read_html(), path_to_images_folder, my_date_format)
    logger.debug(f'added_photo_id_list: {added_photo_id_list}')

    # извлекаю описания снимков и добавляю их в IPTC
    driver.get('https://image.kommersant.ru/photo/archive')
    for photo_id in added_photo_id_list:
        logger.debug(f'Added photo id: {photo_id}')
        image_caption = find_image(photo_id, driver)
        logger.debug(f'{image_caption = }')

        # убираю переносы так как exiftool дает ошибку с ними
        cleaned_image_caption = image_caption.replace("\n", "").replace("\r", "")
        logger.debug(f'{cleaned_image_caption = }')

        uploaded_images_dict[photo_id].append(cleaned_image_caption)
        logger.info(uploaded_images_dict[photo_id])

        # нахожу добавленные снимки на hdd
        find_file_on_hdd(uploaded_images_dict, path_to_images_folder, photo_id, cleaned_image_caption)

    # write_rename_voc(path_to_file, uploaded_images_dict, shoot_id)

    end_selenium(driver)


if __name__ == '__main__':
    main()
