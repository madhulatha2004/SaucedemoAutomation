from selenium.webdriver.common.by import By
import time

class CheckoutPage:

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def checkout(self):
        self.driver.find_element(By.CLASS_NAME, self.config["checkout_button"]).click()
        time.sleep(2)
        self.driver.find_element(By.ID, self.config["first_name"]).send_keys("Madhu")
        self.driver.find_element(By.ID, self.config["last_name"]).send_keys("Putta")
        self.driver.find_element(By.ID, self.config["postal_code"]).send_keys("12345")
        self.driver.find_element(By.CLASS_NAME, self.config["continue_button"]).click()
        time.sleep(2)

    def verify_checkout_items(self):
        checkout_elements = self.driver.find_elements(By.CLASS_NAME, self.config["product_names"])[:4]
        checkout_products = []
        for item in checkout_elements:
            checkout_products.append(item.text)
        return checkout_products

    def finish(self):
        self.driver.find_element(By.CLASS_NAME, self.config["finish_button"]).click()
        time.sleep(2)
        return self.driver.find_element(By.CLASS_NAME, self.config['complete_header']).text

