
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.authorization import AuthorizationHandler


def get_shoot_date(driver, inner_id, shoot_id):

    # open shoot page - without this next link doesn't work
    driver.get(f'https://image.kommersant.ru/photo/archive/search.asp?L=1&code={shoot_id}&ps=100&dt=2&ex=y')

    # open page with information about shoot
    driver.get(f'https://image.kommersant.ru/photo/archive/adm/shoot_read.asp?shootID={inner_id}')


    date_locator = ('xpath', '//span[@id="ShootDate"]')
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(date_locator)
    )

    # get data in Kommersant style
    komm_date = driver.find_element("id", "ShootDate").text[:10].split(
        '.')

    # transform date to my  date format
    my_date_format: str = komm_date[2] + komm_date[1] + komm_date[0]
    return my_date_format


if __name__ == '__main__':
    driver = AuthorizationHandler().authorize()
    print(get_shoot_date(driver, '443182', 'KMO_204282'))