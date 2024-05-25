from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


# page_url = https://the-internet.herokuapp.com/context_menu
class ContextMenuPage(BasePage):
    """LOCATORS"""
    right_click_box_locator = (By.ID, "hot-spot")

    def right_click_on_box(self):
        self.right_click(self.right_click_box_locator)


