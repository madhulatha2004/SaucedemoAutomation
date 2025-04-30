import pytest
import json
from selenium import webdriver


def load_config():
    try:
        with open("./Configurations/config.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print('JSON file not found')
    except KeyError:
        print('Missing key in json file. please check once')
    except ValueError:
        print('Missing value in json file. please check once')


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests: chrome, firefox")


@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("--browser").lower()

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.get("https://www.saucedemo.com/v1")

    config = load_config()
    request.cls.driver = driver
    request.cls.config = config
    yield
    driver.quit()






