import pytest
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass


class BasePage(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    """LOCATORS"""
    successfully_authorized_message = (By.TAG_NAME, "p")

    def find_element_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator),
                                   message=f"Can't find element by locator {locator}")
        except TimeoutException:
            return None

    def find_elements_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_all_elements_located(locator),
                                   message=f"Can't find elements by locator {locator}")
        except TimeoutException:
            return None

    def find_element_clickable(self, locator):
        try:
            return self.wait.until(EC.element_to_be_clickable(locator),
                                   message=f"Can't find clickable element by locator {locator}")
        except TimeoutException:
            return None

    def click(self, locator):
        element = self.find_element_clickable(locator)
        if element:
            element.click()
        else:
            raise Exception(f"Element with locator {locator} is not clickable.")

    def type_text(self, locator, text):
        element = self.find_element_visible(locator)
        if element:
            element.send_keys(text)
        else:
            raise Exception(f"Element with locator {locator} could not be found.")

    def get_text(self, locator):
        element = self.find_element_visible(locator)
        if element:
            return element.text
        else:
            raise Exception(f"Element with locator {locator} could not be found.")

    def get_successfully_authorized_message(self):
        return self.find_element_visible(self.successfully_authorized_message)

    def right_click(self, locator):
        action_chains = ActionChains(self.driver)
        action_chains.context_click(self.find_element_visible(locator)).perform()

    def switch_to_alert(self):
        self.wait.until(EC.alert_is_present(), message="Alert is not present")
        return self.driver.switch_to.alert

    def get_alert_text(self):
        alert = self.switch_to_alert()
        return self.switch_to_alert().text

    def accept_alert(self):
        alert = self.switch_to_alert()
        alert.accept()

    def dismiss_alert(self):
        alert = self.switch_to_alert()
        alert.dismiss()