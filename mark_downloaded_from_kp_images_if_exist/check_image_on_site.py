from selenium.common import NoSuchElementException
from kp_selenium_tools.authorization import AuthorizationHandler


def find_image(image_id):
    driver = AuthorizationHandler().authorize()

    photo_index_locator = ('xpath', "//input[@id='code']")
    driver.find_element(*photo_index_locator).send_keys(image_id)

    button_locator = ('xpath', "//input[@id='searchbtn']")
    driver.find_element(*button_locator).click()

    try:
        images_found_locator = ('xpath', "(//td[@class='note'])[18]")
        images_found = driver.find_element(*images_found_locator).text
        print(images_found)
        return True
    except NoSuchElementException as e:
        print("no images found")
        return False
