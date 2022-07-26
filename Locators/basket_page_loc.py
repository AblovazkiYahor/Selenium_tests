from selenium.webdriver.common.by import By

class BasketPageLoc:
    link_basket = (By.XPATH, "//a[@href='http://automationpractice.com/index.php?controller=order']")

    thing_1 = (By.ID, 'summary_products_quantity')