import pytest
from PageObjects.Login_page import LoginPage
from testCases.conftest import setup
from utilities.customLogger import LogGen


@pytest.mark.usefixtures("setup")
class TestSauceDemo:

    logger = LogGen.loggen()


    def test_login_page_title(self):
        self.logger.info("******************** Test_001_login *****************")
        self.logger.info("******************** Verifying Home Page Title *****************")
        actual_title = self.driver.title
        expected_title = 'Swag Labs'
        if actual_title == expected_title:
            assert True
            self.logger.info("******************** Home Page title test is passed *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_page_title.png")
            self.logger.error("******************** Home Page title test is failed *****************")
            assert False


    @pytest.mark.parametrize("username,password,expected", [
        ("standard_user", "secret_sauce", True),
        ("problem_user", "secret_sauce", True),
        ("locked_out_user", "secret_sauce", False),
        ("performance_glitch_user", "secret_sauce", True),
        ("invalid_user", "secret_sauce", False),
        ("standard_user", "wrong_pass", False),
        ("", "secret_sauce", False),
        ("standard_user", "", False),
    ])
    def test_login_scenarios(self, username, password, expected):
        self.logger.info("******************** Checking login test **********************")
        login = LoginPage(self.driver, self.config)
        self.driver.get(self.config["baseURL"])
        success = login.login(username, password)
        if success == expected:
            assert True
            self.logger.info("******************** Login test is passed *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login_scenarios.png")
            self.logger.error("******************** Login test is failed *****************")
            assert False



