from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


# page_url = https://the-internet.herokuapp.com/broken_images
class BrokenImagesPage(BasePage):
    """LOCATORS"""
    broken_images = (By.XPATH, "//div[@class='example']/img")

    def get_broken_images(self):
        return self.find_elements_visible(self.broken_images)

