import pytest
from site_1_task1 import test_value
from selenium.webdriver.common.by import By





dropdown_test = chrome.find_element(By.XPATH, "//*[contains(text(), 'Group 1, option 1')]").text
drop_test_1 = 'Group 1, option 1'
assert dropdown_test == drop_test_1

dropdown_inf_1 = chrome.find_element(By.XPATH, "//*[contains(text(), 'Dr.')]").text
drop_test_2 = 'Dr.1'
assert dropdown_inf_1 == drop_test_2

dropdown_old_1 = chrome.find_element(By.XPATH, "//*[contains(text(), 'Green')]").text
drop_test_3 = 'Green'
assert dropdown_old_1 == drop_test_3

value_multi = chrome.find_element(By.XPATH, "//*[contains(text(), 'Black')]").text
drop_test_4 = 'Black'
assert drop_test_4 == value_multi

value_multi = chrome.find_element(By.XPATH, "//*[contains(text(), 'Black')]").text
drop_test_4 = 'White'
assert drop_test_4 == value_multi