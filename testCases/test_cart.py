import pytest
from PageObjects.Login_page import LoginPage
from PageObjects.InventoryPage import InventoryPage
from PageObjects.cart_page import CartPage
from selenium.webdriver.common.by import By
from utilities.customLogger import LogGen

@pytest.mark.usefixtures("setup")
class TestInventory:
    logger = LogGen.loggen()

    def login(self, username="standard_user", password="secret_sauce"):
        login_page = LoginPage(self.driver, self.config)
        login_page.login(username, password)

    def test_verify_cart(self):
        self.logger.info("******************** Test_001_cart *****************")
        self.logger.info("******************** Verifying cart products *****************")
        self.driver.get(self.config["baseURL"])
        self.login()
        inventory = InventoryPage(self.driver, self.config)
        selected_products = inventory.add_to_cart()
        cart = CartPage(self.driver, self.config)
        cart_products = cart.verify_cart()
        if cart_products == selected_products:
            assert True
            self.logger.info("******************** Cart products verification test is passed *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_verify_cart.png")
            self.logger.error("******************** Cart products verification test is failed *****************")
            assert False
        cart.remove_all()

    def test_cart_is_empty_default(self):
        self.logger.info("******************** Verifying cart is empty by default *****************")
        self.driver.get(self.config["baseURL"])
        self.login()
        cart = CartPage(self.driver, self.config)
        cart.remove_all()
        cart_products = cart.verify_cart()
        if len(cart_products) == 0:
            assert True
            self.logger.info("******************** verifying cart is empty test is passed *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_cart_is_empty_default.png")
            self.logger.error("******************** verifying cart is empty  test is failed *****************")
            assert False

    def test_remove_from_cart(self):
        self.logger.info("******************** Removing products from cart *****************")
        self.driver.get(self.config["baseURL"])
        self.login()
        inventory = InventoryPage(self.driver, self.config)
        inventory.add_to_cart()
        cart = CartPage(self.driver, self.config)
        cart.remove_all()
        cart_after_remove = self.driver.find_elements(By.CLASS_NAME, 'cart_item')
        if len(cart_after_remove) == 0:
            assert True
            self.logger.info("******************** Removing products from cart test is passed *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_remove_from_cart.png")
            self.logger.error("******************** Removing products from cart test is failed *****************")
            assert False




