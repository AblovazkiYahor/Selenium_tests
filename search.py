
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.common.by import By
import time


def test_input_search():
    url = 'https://demoqa.com/text-box'
    chrome = webdriver.Chrome(ChromeDriverManager().install())
    chrome.get(url)
    search_input_field_1 = chrome.find_element(By.ID, 'userName')
    search_input_field_1.send_keys('Egor')
    time.sleep(2)
    search_input_field_2 = chrome.find_element(By.ID, 'userEmail')
    search_input_field_2.send_keys('egor@gmal.com')
    time.sleep(2)
    search_input_cur_adress = chrome.find_element(By.ID, 'currentAddress')
    search_input_cur_adress.send_keys('Pobedy, 21')
    time.sleep(2)
    search_input_per_adress = chrome.find_element(By.ID, 'permanentAddress')
    search_input_per_adress.send_keys('Pobediteley, 25')
    time.sleep(2)

    button = chrome.find_element(By.ID, 'submit')
    time.sleep(2)
    button.click()

    table = chrome.find_element(By.ID, 'name').text
    fullName = 'Name:Egor'
    assert fullName == table

    table2 = chrome.find_element(By.CLASS_NAME, 'email').text
    name_email = 'egor@gmal.com'
    assert table2 == name_email

    table3 = chrome.find_element(By.ID, 'currentAddress').text
    addres1 = 'Current Address :Pobedy, 21'
    assert table3 == addres1

    table4 = chrome.find_element(By.ID, 'permanentAddress').text
    addres2 = 'Permananet Address :Pobediteley, 25'
    assert table4 == addres2


