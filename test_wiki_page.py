from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_wiki_page_search():
    url = 'https://ru.wikipedia.org/wiki/'
    chrome = webdriver.Chrome('chromedriver')
    word = 'Автоматизация'
    chrome.get(url)
    time.sleep(2)
    search_input = chrome.find_elements(By.ID, 'searchInput')
    search_input.send_keys(word)
    search_input.submit()
    time.sleep(2)
    title = chrome.find_elements(By.ID, 'firstHeading').text
    assert word == title, f'{title} is not eq {word}'
