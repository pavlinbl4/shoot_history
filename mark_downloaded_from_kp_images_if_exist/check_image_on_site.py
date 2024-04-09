from selenium.common import NoSuchElementException

'''
браузер должен быть запущен, чтоб не проходить авторизацию для каждого снимка заново
скрипт вводит photo_id  в поле поиска, если снимок найден возвращает True, если нет, то False
'''


def find_image(image_id, driver):
    photo_search_index_locator = ('xpath', "//input[@id='code']")
    driver.find_element(*photo_search_index_locator).send_keys(image_id)

    search_button_locator = ('xpath', "//input[@id='searchbtn']")
    driver.find_element(*search_button_locator).click()

    try:
        images_found_locator = ('xpath', "(//td[@class='note'])[18]")
        driver.find_element(*images_found_locator)
        print(f'image {image_id} is on site')
        return True
    except NoSuchElementException as e:
        print(f"image {image_id} not found")
        return False
