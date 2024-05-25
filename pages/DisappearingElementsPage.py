from selenium.webdriver.common.by import By


# page_url = https://the-internet.herokuapp.com/disappearing_elements
class DisappearingElementsPage(object):
    def __init__(self, driver):
        self.driver = driver

