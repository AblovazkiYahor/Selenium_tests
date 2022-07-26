from selenium import webdriver
from selenium.webdriver.common.by import By
import math



def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def test_maths():
    url = 'http://suninjuly.github.io/math.html'
    chrome = webdriver.Chrome('chromedriver')
    chrome.get(url)
    x = chrome.find_element(By.ID, 'input_value').text
    res = calc(x)
    f = chrome.find_element(By.ID, 'answer')
    f.send_keys(f'{res}')

    check = chrome.find_element(By.CLASS_NAME, 'form-check-input')
    check.click()

    radio = chrome.find_element(By.ID, 'robotsRule')
    radio.click()

    button = chrome.find_element(By.CLASS_NAME, "btn, btn-default")
    button.click()




