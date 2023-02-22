import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


username = 'LiuxGf'

passward = 'lx19951022lxGf'

loginUrl = 'http://39.107.108.81/qjwzwb/login/login_qt.htm'
url = 'http://39.107.108.81/qjwzwb/stulogin/input.htm'

idxDict = [
    '2023006577', '2023006578', '2023008244',
    '2023008829', '2023025363', '2023025364',
    '2023025365', '2023025366', '2023025373',
    '2023025375', '2023025565', '2023025566',
    '2023006535', '2023006553', '2023006580',
    '2023006581', '2023025567', '2023019027',
    '2023019034', '2023019043', '2023019045',
    '2023020001', '2023020002'
]


def getInfo():
    resultDict = {}
    driver_test = webdriver.Edge()
    driver_test.get(loginUrl)
    driver_test.find_element(By.CSS_SELECTOR,
                             'input[id="yusername"]').send_keys(username)
    time.sleep(4)
    driver_test.find_element(By.CSS_SELECTOR,
                             'input[id="ypassword"]').send_keys(passward)
    time.sleep(5)

    driver_test.find_element(By.CSS_SELECTOR,
                             'input[type="button"]').click()
    time.sleep(10)

    for idx in idxDict:
        driver_test.find_element(By.CSS_SELECTOR,
                                 'input[name="queryCon"]').clear()
        driver_test.find_element(By.CSS_SELECTOR,
                                 'input[name="queryCon"]').send_keys(idx, Keys.ENTER)
        time.sleep(3)

        num = driver_test.find_element(By.CSS_SELECTOR,
                                       'td[id="show_zprs"]').text
        resultDict[idx] = num
        print(idx, ": ", num)


if __name__ == '__main__':
    getInfo()
