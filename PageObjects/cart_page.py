from selenium.webdriver.common.by import By
import time

class CartPage:

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def verify_cart(self):
        self.driver.find_element(By.CLASS_NAME, self.config["cart_link"]).click()
        time.sleep(2)
        cart_elements = self.driver.find_elements(By.CLASS_NAME, self.config["product_names"])
        cart_products = []
        for item in cart_elements:
            cart_products.append(item.text)
        return cart_products

    def remove_all(self):
        self.driver.find_element(By.CLASS_NAME, self.config['cart_link']).click()
        remove_buttons = self.driver.find_elements(By.CLASS_NAME, 'btn_secondary.cart_button')
        for btn in remove_buttons:
            btn.click()


