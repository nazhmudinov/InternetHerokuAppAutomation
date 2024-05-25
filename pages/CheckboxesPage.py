from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


# page_url = https://the-internet.herokuapp.com/checkboxes
class CheckboxesPage(BasePage):
    """LOCATORS"""
    @staticmethod
    def get_checkboxes_by_index(index):
        return By.XPATH, f"//input[@type='checkbox'][{index}]"

    def get_checkbox_by_index(self, index):
        return self.find_element_visible(self.get_checkboxes_by_index(index))

    def select_checkbox(self, index):
        checkbox = self.get_checkboxes_by_index(index)
        self.click(checkbox)