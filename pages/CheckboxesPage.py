from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


# page_url = https://the-internet.herokuapp.com/checkboxes
class Checkboxes(BasePage):
    """LOCATORS"""
    checkboxes = (By.CSS_SELECTOR, "input[type='checkbox']")

    def select_checkbox(self, index):
        self.click(self.checkboxes[index])

