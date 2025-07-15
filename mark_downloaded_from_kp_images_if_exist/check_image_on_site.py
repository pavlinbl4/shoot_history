from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

'''
браузер должен быть запущен, чтоб не проходить авторизацию для каждого снимка заново
скрипт вводит photo_id  в поле поиска, если снимок найден возвращает True, если нет, то False
'''


def grab_image_caption(driver):
    caption_found_locator = ('xpath', "(//td[@class='main'])[3]/p[@class='txt']")

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(caption_found_locator)
    )
    return driver.find_element(*caption_found_locator).text


def find_image(image_id, driver):
    try:
        photo_search_index_locator = ('xpath', "//input[@id='code']")

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(photo_search_index_locator)
        )

        driver.find_element(*photo_search_index_locator).clear()
        driver.find_element(*photo_search_index_locator).send_keys(image_id)

        search_button_locator = ('xpath', "//input[@id='searchbtn']")
        driver.find_element(*search_button_locator).click()

        try:
            images_found_locator = ('xpath', "(//td[@class='note'])[18]")

            WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located(images_found_locator)
            )

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
