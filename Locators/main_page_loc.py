from selenium.webdriver.common.by import By


class MainPageLoc:

    login_loc = (By.CSS_SELECTOR, ".login")
    basket_empty_loc = (By.XPATH, '//div[@class="shopping_cart"]//span[contains(text(), "(empty)")]')
    first_thing_loc = (By.XPATH, '//*[@id="header"]/div[3]/div/div/div[3]/div/a')
    second_thing_loc = (By.XPATH, '//*[@id="homefeatured"]/li[2]/div/div[2]/div[2]/a[1]')
    close_popup_x = (By.CLASS_NAME, 'cross')