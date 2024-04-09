"""
Work with the image description page that is
available when you press the button with the hammer and wrench icon.
"""


from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By




def add_new_keywords(concatinated_keywords):
    if 'софт' in concatinated_keywords:
        return concatinated_keywords + ", " + 'цифровизация'
    if 'импортозамещение' in concatinated_keywords:
        return concatinated_keywords + ", " + 'импортоопережение'
    if "цифровизация" in concatinated_keywords:
        return concatinated_keywords + ", " + 'компьютеризация'


def set_keywords_to_site(good_keywords, driver):
    # main_window = driver.current_window_handle
    # try:
    driver.find_element(By.NAME, 'KeywordsRus').clear()
    driver.find_element(By.NAME, 'KeywordsRus').send_keys(good_keywords)
    driver.find_element(By.NAME, 'Add').click()

    # wait = WebDriverWait(driver, 1)
    # alert = wait.until(EC.alert_is_present())
    #
    # if alert:
    #     alert.accept()

    # except TimeoutException:
    #     print('no TimeoutException')

    # driver.switch_to.window(main_window)
    # driver.find_element(By.ID, 'DescriptionRus').click()
    # driver.find_element(By.ID, 'DescriptionRus').send_keys('требуется описание')
    # driver.find_element(By.NAME, 'Add').click()


def grab_image_info_page(driver, info_page_url):
    try:
        driver.get(info_page_url)
        keywords = driver.find_element(By.ID, 'KeywordsRus').get_attribute('value')
        image_id = driver.find_element(By.ID, 'photoPreview').find_element(By.TAG_NAME, 'span').text
        caption = driver.find_element(By.ID, 'DescriptionRus').get_attribute('value')

    except NoSuchElementException:
        print("One of the elements was not found on the page")
        return None, None, None

    return image_id, caption, keywords


# def image_info_optimization(driver, text_edit_link):
#     image_id, caption, keywords = grab_image_info_page(driver, text_edit_link)  # grab info
#
#     # if keywords not empty - optimise it
#     if keywords != '' and keywords is not None:
#         write_kp_files_keywords(image_id, caption, keywords)  # save data in csv file
#
#         keywords_from_caption = ", ".join(lema(caption))
#
#         concatinated_keywords = keywords_from_caption + ", " + keywords  # concatinate keywords
#
#         add_new_keywords(concatinated_keywords)
#
#         # optimized_keywords = keywords_opimization(keywords)  # replace ; with comma
#         optimized_keywords = keywords_opimization(concatinated_keywords)  # replace ; with comma
#
#         print(optimized_keywords)
#
#         set_keywords_to_site(optimized_keywords, driver)  # write optimized keywords to site
#     elif keywords == '':
#         #  if no keywords lemmatize caption
#         keywords_from_caption = ", ".join(lema(caption))
#
#         set_keywords_to_site(keywords_from_caption, driver)  # write  keywords  from caption to site
#
#         write_kp_files_keywords(image_id, keywords_from_caption, keywords)  # save data in csv file
#
#
# if __name__ == '__main__':
#     t_driver = autorization()
#
#     image_info_optimization(t_driver,
#                             'https://image.kommersant.ru/photo/archive/adm/AddPhotoStep3.asp?ID=3791347&CloseForm=1')
