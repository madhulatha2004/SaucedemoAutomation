import pytest
from PageObjects.Login_page import LoginPage
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

@pytest.mark.usefixtures("setup")
class TestSauceDemo:
    path = ".//TestData/login_data.xlsx"
    logger = LogGen.loggen()

    def test_login_scenarios(self):
        self.logger.info("******************** Test_001_login *****************")
        self.logger.info("******************** Checking login test **********************")
        self.lp = LoginPage(self.driver, self.config)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print('Number of Rows in Excel:', self.rows)

        lst_status = []
        for r in range(2, self.rows + 1):
            username = XLUtils.readData(self.path, 'Sheet1', r, 1)
            password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            expected_status = XLUtils.readData(self.path, 'Sheet1', r, 3)
            if username is None:
                username = ''
            if password is None:
                password = ''
            self.driver.get(self.config["baseURL"])
            time.sleep(1)
            self.lp.login(username, password)

            actual_url = self.driver.current_url
            exp_url= "https://www.saucedemo.com/v1/inventory.html"

            if actual_url == exp_url:
                if expected_status =='Pass':
                    self.logger.info(f"************* Login Test Passed for {username} ************")
                    self.lp.logout()
                    lst_status.append('Pass')
                elif expected_status =='Fail':
                    self.logger.info(f"************* Login Test Failed for {username} ************")
                    self.lp.logout()
                    lst_status.append('Fail')
            elif actual_url != exp_url:
                if expected_status == 'Pass':
                    self.logger.info(f"************* Login Test Failed for {username} ************")
                    self.lp.logout()
                    lst_status.append('Fail')
                elif expected_status == 'Fail':
                    self.logger.info(f"*********** Login Test passed for {username} **********")
                    self.lp.logout()
                    lst_status.append('Pass')
        if 'Fail' not in lst_status:
            self.logger.info('***************** Login test passed ***************')
            self.driver.quit()
            assert True
        else:
            self.logger.error('*************** Login test failed ***************')
            self.driver.quit()
            assert False
