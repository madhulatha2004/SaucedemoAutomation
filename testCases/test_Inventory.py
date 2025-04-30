import pytest
from PageObjects.Login_page import LoginPage
from PageObjects.InventoryPage import InventoryPage
from utilities.customLogger import LogGen

@pytest.mark.usefixtures("setup")
class TestInventory:
    logger = LogGen.loggen()


    def test_login_and_open_inventory(self):
        self.logger.info("******************** Test_001_Inventory *****************")
        self.logger.info("******************** Verifying inventory Home Page Title *****************")
        self.driver.get(self.config["baseURL"])
        login = LoginPage(self.driver, self.config)
        login.login("standard_user", "secret_sauce")
        if self.driver.title == "Swag Labs":
            assert True
            self.logger.info("******************** Inventory Home Page title test is passed *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_and_open_inventory.png")
            self.logger.error("******************** Inventory Home Page title test is failed *****************")
            assert False

    def test_product_details_loaded(self):
        self.logger.info("******************** Verifying product details *****************")
        inventory = InventoryPage(self.driver, self.config)
        product_names, product_prices = inventory.product_details()
        assert len(product_names) > 0
        assert len(product_prices) > 0

    def test_add_first_4_products_to_cart(self):
        self.logger.info("******************** Adding products to cart *****************")
        inventory = InventoryPage(self.driver, self.config)
        selected = inventory.add_to_cart()
        if len(selected) == 4:
            assert True
            self.logger.info("******************** Adding products to cart test is passed *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_add_first_4_products_to_cart.png")
            self.logger.error("******************** Adding products to cart test is failed *****************")
            assert False





