from selenium.common import NoSuchElementException

from kp_selenium_tools.authorization import AuthorizationHandler
from kp_selenium_tools.selenium_tools import end_selenium

'''
браузер должен быть запущен, чтоб не проходить авторизацию для каждого снимка заново
скрипт вводит photo_id  в поле поиска, если снимок найден возвращает True, если нет, то False
'''


def grab_image_caption(driver):
    caption_found_locator = ('xpath', "(//td[@class='main'])[3]/p[@class='txt']")
    return driver.find_element(*caption_found_locator).text


def find_image(image_id, driver):
    try:
        photo_search_index_locator = ('xpath', "//input[@id='code']")
        driver.find_element(*photo_search_index_locator).clear()
        driver.find_element(*photo_search_index_locator).send_keys(image_id)

        search_button_locator = ('xpath', "//input[@id='searchbtn']")
        driver.find_element(*search_button_locator).click()

        try:
            images_found_locator = ('xpath', "(//td[@class='note'])[18]")
            driver.find_element(*images_found_locator)
            # print(f'image {image_id} is on site')

            # извлекаю описание снимка с сайта
            image_caption = grab_image_caption(driver)

            return image_caption

        except NoSuchElementException as e:
            print(f"image {image_id} not found")
            return False
    except NoSuchElementException as e:
        print(e)


if __name__ == '__main__':
    _driver = AuthorizationHandler().authorize()

    print(find_image('KSP_018323_00051_1', _driver))

    end_selenium(_driver)
