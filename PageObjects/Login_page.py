from selenium.webdriver.common.by import By
import time

class LoginPage:

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def get_information(self):
        username_element = self.driver.find_element(By.CLASS_NAME, self.config['usernames_extract'])
        password_element = self.driver.find_element(By.CLASS_NAME, self.config['password_extract'])
        usernames = username_element.text.split("\n")[1:]
        password = password_element.text.split("\n")[1]
        return usernames, password


    def login(self, username, password):
        username_input = self.driver.find_element(By.CLASS_NAME, self.config["username_field"])
        password_input = self.driver.find_element(By.ID, self.config["password_field"])
        login_button = self.driver.find_element(By.ID, self.config["login_button"])
        username_input.clear()
        username_input.send_keys(username)
        password_input.clear()
        password_input.send_keys(password)
        login_button.click()
        time.sleep(1)
        try:
            self.driver.find_element(By.CLASS_NAME, self.config["product_names"])
            print(f"Login successful with username: {username}")
            return True
        except:
            print(f"Login failed with username: {username}")
            return False

    def logout(self):
        try:
            self.driver.find_element(By.CLASS_NAME, self.config['menu_button']).click()
            time.sleep(1)
            self.driver.find_element(By.ID, self.config['logout_button']).click()
            time.sleep(1)
            print('Logout successfull')
        except Exception as e:
            print('Logout Failed')
