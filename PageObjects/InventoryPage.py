from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class InventoryPage:

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def product_details(self):
        default_product_names = []
        default_product_prices = []
        product_names = self.driver.find_elements(By.CLASS_NAME, self.config["product_names"])
        product_prices = self.driver.find_elements(By.CLASS_NAME, self.config["product_prices"])
        for product in product_names:
            default_product_names.append(product.text)
        for price in product_prices:
            default_product_prices.append(float(price.text.replace('$', '')))
        return product_names, product_prices


    def verify_sorting(self):
        default_names, default_prices = self.product_details()
        sort_dropdown = Select(self.driver.find_element(By.CLASS_NAME, self.config["product_sort_dropdown"]))
        sort_options = []
        for option in sort_dropdown.options:
            sort_options.append(option.text)

        for option in sort_options[1:]:
            sort_dropdown.select_by_visible_text(option)
            time.sleep(2)
            sorted_names, sorted_prices = self.product_details()
            if sorted_names != default_names or sorted_prices != default_prices:
                print(f"Sorting applied: {option} → Product order changed.")
            else:
                print(f"Sorting applied: {option} → No changes in product order.")

    def add_to_cart(self):
        product_elements = self.driver.find_elements(By.CLASS_NAME, self.config['product_names'])[:4]
        add_buttons = self.driver.find_elements(By.CLASS_NAME, self.config["add_to_cart_buttons"])[:4]
        selected_products = []
        for product in product_elements:
            selected_products.append(product.text)
        for button in add_buttons:
            button.click()
            time.sleep(1)
        return selected_products