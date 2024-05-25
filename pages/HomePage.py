from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


# page_url = https://the-internet.herokuapp.com/
class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """LOCATORS"""
    main_header = (By.CSS_SELECTOR, "heading")
    main_content = (By.ID, "content")
    link_add_remove_elements = (By.LINK_TEXT, "Add/Remove Elements")
    basic_auth = (By.LINK_TEXT, "Basic Auth")
    broken_images = (By.LINK_TEXT, "Broken Images")
    checkboxes = (By.LINK_TEXT, "Checkboxes")
    context_menu = (By.LINK_TEXT, "Context Menu")
    disappearing_elements = (By.LINK_TEXT, "Disappearing Elements")

    def header_visible(self):
        return self.find_element_visible(self.main_content)

    def content_visible(self):
        return self.find_element_visible(self.main_content)

    def click_link_add_remove_elements(self):
        self.click(self.link_add_remove_elements)

    def click_basic_auth(self):
        self.click(self.basic_auth)

    def click_broken_images(self):
        self.click(self.broken_images)

    def click_checkboxes(self):
        self.click(self.checkboxes)

    def click_context_menu(self):
        self.click(self.context_menu)

    def click_disappearing_elements(self):
        self.click(self.disappearing_elements)
