import pytest

from Main_page import MainPage
from Locators.main_page_loc import MainPageLoc
from Locators.basket_page_loc import BasketPageLoc
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class BasketPage(MainPage):

    def open_login_page(self):
        login_link = self.chrome.find_element(MainPageLoc.login_loc)
        login_link.click()

    # def verify_login_url(self):

    def verify_login_link(self):
        assert self.is_element_present(MainPageLoc.login_loc), "Element is absent!"

    def verify_basket_is_empty(self):
        assert self.is_element_present(MainPageLoc.basket_empty_loc), "Basket is not empty"

    def open_basket_page(self):
        basket_link = self.chrome.find_element(BasketPageLoc.link_basket)
        basket_link.click()

        assert self.is_element_present(BasketPageLoc.thing_1), 'Basket is empty'