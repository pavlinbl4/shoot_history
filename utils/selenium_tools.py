from selenium.webdriver.common.by import By

from utils.make_page_link import make_history_link, get_inner_id


def open_page(page_link, browser):
    browser.get(page_link)


def extract_data_from_page(driver):
    driver.find_element(By.ID, 'ctl00_MainContent_ShootInfoForm_FullShootNumber').click()
    driver.find_element(By.CLASS_NAME, 'history-header').click()
    shoot_history_link = driver.current_url

    inner_id = get_inner_id(shoot_history_link)


    full_link = make_history_link(inner_id)  # получаю ссылку на страницу с подробной историей
    driver.get(full_link)  # открывается новая вкладка, нужно перейти на нее
    driver.switch_to.window(driver.window_handles[0])

    with open(f'tests/test_files/test_file.html', 'w', encoding='utf-8') as file:
        file.write(driver.page_source)

    return driver.page_source, inner_id



def end_selenium(driver):
    driver.close()
    driver.quit()
