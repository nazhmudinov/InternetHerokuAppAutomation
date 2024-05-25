from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


# page_url = https://the-internet.herokuapp.com/add_remove_elements/
class AddRemoveElementsPage(BasePage):
    """LOCATORS"""
    header = (By.XPATH, "//h3")
    button_add_element = (By.CSS_SELECTOR, "button[onclick='addElement()']")
    button_remove_element = (By.CSS_SELECTOR, "button[onclick='deleteElement()']")

    def click_add_element(self):
        self.click(self.button_add_element)

    def get_remove_element(self):
        return self.find_element_visible(self.button_remove_element)

    def click_remove_element(self):
        self.click(self.button_remove_element)

