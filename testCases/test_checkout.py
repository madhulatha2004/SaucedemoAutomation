import pytest
from PageObjects.cart_page import CartPage
from PageObjects.checkout_page import CheckoutPage
from PageObjects.Login_page import LoginPage
from PageObjects.InventoryPage import InventoryPage
from utilities.customLogger import LogGen

@pytest.mark.usefixtures("setup")
class TestCheckout:
    logger = LogGen.loggen()

    def login(self, username="standard_user", password="secret_sauce"):
        login_page = LoginPage(self.driver, self.config)
        login_page.login(username, password)
        inventory = InventoryPage(self.driver, self.config)
        cart = CartPage(self.driver, self.config)
        selected_products = inventory.add_to_cart()
        cart.verify_cart()
        return selected_products


    def test_checkout_form_submission(self):
        self.logger.info("******************** Test_001_checkout *****************")
        self.logger.info("******************** Verifying checkout Page url *****************")
        self.login()
        checkout = CheckoutPage(self.driver, self.config)
        checkout.checkout()
        if "checkout-step-two" in self.driver.current_url:
            assert True
            self.logger.info("******************** Checkout page url test is passed *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_checkout_form_submission.png")
            self.logger.error("******************** Checkout page url test is failed *****************")
            assert False
        checkout.finish()

    def test_verify_checkout_items(self):
        self.logger.info("******************** Verifying checkout items *****************")
        self.driver.get(self.config["baseURL"])
        selected_products = self.login()
        checkout = CheckoutPage(self.driver, self.config)
        checkout.checkout()
        actual_products = checkout.verify_checkout_items()
        if actual_products == selected_products:
            assert True
            self.logger.info("******************** checkout items verification test is passed *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_verify_checkout_items.png")
            self.logger.error("******************** checkout items verification test is failed *****************")
            assert False
        cart = CartPage(self.driver, self.config)
        cart.remove_all()

    def test_finish_button_completes_purchase(self):
        self.logger.info("******************** Verifying finish button *****************")
        self.driver.get(self.config["baseURL"])
        self.login()
        checkout = CheckoutPage(self.driver, self.config)
        checkout.checkout()
        confirmation_text = checkout.finish()
        if confirmation_text == "THANK YOU FOR YOUR ORDER":
            assert True
            self.logger.info("******************** Verifying finish button test is passed *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_finish_button_completes_purchase.png")
            self.logger.error("******************** Verifying finish button test is failed *****************")
            assert False
