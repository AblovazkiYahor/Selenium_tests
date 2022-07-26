import pytest

from Main_page import MainPage
from Basket_page import BasketPage
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def open_browser():
    global browser
    browser = webdriver.Chrome(ChromeDriverManager().install())


def test_basket_is_empty(open_browser):
    link = "http://automationpractice.com/index.php"
    Main_page = MainPage(browser, link)

    try:
        Main_page.open()
        Main_page.verify_basket_is_empty()
    finally:
        browser.quit()

def test_add_things(open_browser):
    link = "http://automationpractice.com/index.php"
    Main_page = MainPage(browser, link)

    try:
        Main_page.open()
        Main_page.verify_basket_is_empty()
        Main_page.add_things()
        Main_page.second_things()
        BasketPage.open_basket_page()


    finally:
        browser.quit()



