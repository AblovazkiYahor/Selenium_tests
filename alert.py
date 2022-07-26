from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_alert():
    url = 'http://suninjuly.github.io/alert_accept.html'
    chrome = webdriver.Chrome('chromedriver')
    chrome.get(url)

    chrome.find_element(By.CLASS_NAME, 'btn, btn-primary').click()
    alert = chrome.switch_to.alert
    alert.accept()



