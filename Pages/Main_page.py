from Base_page import BasePage
from Locators.main_page_loc import MainPageLoc


class MainPage(BasePage):

    def open_login_page(self):
        login_link = self.chrome.find_element(MainPageLoc.login_loc)
        login_link.click()

    # def verify_login_url(self):

    def verify_login_link(self):
        assert self.is_element_present(MainPageLoc.login_loc), "Element is absent!"

    def verify_basket_is_empty(self):
        assert self.is_element_present(MainPageLoc.basket_empty_loc), "Basket is not empty"

    def add_things(self):
        add_first_things = self.chrome.find_element(MainPageLoc.first_thing_loc)
        add_first_things.click()

        close_popup = self.chrome.find_element(MainPageLoc.close_popup_x)
        close_popup.click()

    def second_things(self):
        add_second_things = self.chrome.find_element(MainPageLoc.second_thing_loc)
        add_second_things.click()

        close_popup = self.chrome.find_element(MainPageLoc.close_popup_x)
        close_popup.click()




