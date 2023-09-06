from selenium.webdriver.common.by import By
from kp_selenium_tools.make_page_link import make_history_link


red = '\033[91m'
green = '\33[32m'
end = '\033[0m'


def open_page(page_link, browser):
    browser.get(page_link)


def work_to_history(driver):
    driver.find_element(By.ID, 'ctl00_MainContent_ShootInfoForm_FullShootNumber').click()
    driver.find_element(By.CLASS_NAME, 'history-header').click()
    first_link = driver.current_url
    full_link = make_history_link(first_link)  # получаю ссылку на страницу с подробной историей
    driver.get(full_link)  # открывается новая вкладка, нужно перейти на нее
    driver.switch_to.window(driver.window_handles[0])
    return driver.page_source


def end_selenium(driver):
    driver.close()
    driver.quit()
