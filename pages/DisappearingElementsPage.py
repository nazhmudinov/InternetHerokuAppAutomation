from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


# page_url = https://the-internet.herokuapp.com/disappearing_elements
class DisappearingElementsPage(BasePage):
    """LOCATORS"""
    disappearing_elements = (By.XPATH, "//div[@class='example']//a")

    def get_disappearing_elements_length(self):
        return len(self.find_elements_visible(self.disappearing_elements))
