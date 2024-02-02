from auto_webdriver.update_driver import auto_update_webdriver
from kp_selenium_tools.authorization import AuthorizationHandler

from kp_selenium_tools.choose_input import clipboard_or_input
from kp_selenium_tools.make_page_link import make_page_link
from kp_selenium_tools.save_page_html import save_html_page, read_html
from kp_selenium_tools.selenium_tools import open_page, work_to_history, end_selenium
from kp_selenium_tools.tk_tools import select_folder_via_gui
from kp_selenium_tools.write_xlsx import write_rename_voc
from shoot_history.scrap_html import scrap_html



def main():
    auto_update_webdriver()

    path_to_file = '/Users/evgeniy/Documents/Kommersant/shoot_rename/shoot_story.xlsx'

    shoot_id = clipboard_or_input()

    path = select_folder_via_gui('/Users/evgeniy/Pictures/2024')

    driver = AuthorizationHandler().authorize()

    page_link = make_page_link(shoot_id)

    open_page(page_link, driver)

    full_history_page_source = work_to_history(driver)  # получаю данные со страницы истории

    save_html_page(full_history_page_source)  # временно сохраняю страницу

    file_renames = scrap_html(read_html(), path)  # path to folder with images

    write_rename_voc(path_to_file, file_renames, shoot_id)

    end_selenium(driver)


if __name__ == '__main__':
    main()
