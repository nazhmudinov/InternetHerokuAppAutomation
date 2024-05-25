import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class BasePage:
    def __init__(self, driver):
        self.driver = driver


