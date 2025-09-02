from selenium.webdriver.common.by import By
from loguru import logger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.make_page_link import make_history_link, get_inner_id


def extract_data_from_page(driver):
    WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.ID, 'ctl00_MainContent_ShootInfoForm_FullShootNumber'))
    )
    driver.find_element(By.ID, 'ctl00_MainContent_ShootInfoForm_FullShootNumber').click()

    driver.find_element(By.CLASS_NAME, 'history-header').click()
    shoot_history_link = driver.current_url

    inner_id = get_inner_id(shoot_history_link)
    logger.debug(f'inner id: {inner_id}')

    full_link = make_history_link(inner_id)  # получаю ссылку на страницу с подробной историей
    driver.get(full_link)  # открывается новая вкладка, нужно перейти на нее
    driver.switch_to.window(driver.window_handles[0])

    with open(f'tests/test_files/test_file.html', 'w', encoding='utf-8') as file:
        file.write(driver.page_source)

    return driver.page_source, inner_id


def end_selenium(driver):
    driver.close()
    driver.quit()
