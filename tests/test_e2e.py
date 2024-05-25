import base64
import time
from pages.AddRemoveElementsPage import AddRemoveElementsPage
from pages.BasePage import BasePage
from pages.BrokenImagesPage import BrokenImagesPage
from pages.CheckboxesPage import CheckboxesPage
from pages.ContextMenuPage import ContextMenuPage
from pages.DisappearingElementsPage import DisappearingElementsPage
from pages.HomePage import HomePage
from utilities.BaseClass import BaseClass
import requests


class TestE2e(BaseClass):
    def test_content_visible(self):
        homepage = HomePage(self.driver)
        assert homepage.header_visible(), "Header is not visible"
        assert homepage.content_visible(), "Content is not visible"

    def test_add_remove_elements(self):
        homepage = HomePage(self.driver)
        page = AddRemoveElementsPage(self.driver)
        homepage.click_link_add_remove_elements()

        try:
            page.click_add_element()
            assert page.get_remove_element().is_displayed(), "Remove element button was not found"
        finally:
            page.click_remove_element()
            assert page.get_remove_element() is None, "Remove button is still displayed"

        self.driver.back()

    def test_http_basic_auth(self):
        homepage = HomePage(self.driver)
        basepage = BasePage(self.driver)
        # Enable the Network domain using Chrome DevTools Protocol
        self.driver.execute_cdp_cmd("Network.enable", {})
        # Encode the credentials using Base64
        credentials = base64.b64encode("admin:admin".encode()).decode()
        # Prepare the headers with the encoded credentials
        headers = {'headers': {'authorization': 'Basic ' + credentials}}
        # Set the extra HTTP headers for all network requests
        self.driver.execute_cdp_cmd('Network.setExtraHTTPHeaders', headers)
        homepage.click_basic_auth()
        expected_success_text = basepage.get_successfully_authorized_message().text
        assert "Congratulations" in expected_success_text

        self.driver.back()

    def test_broken_images(self):
        homepage = HomePage(self.driver)
        page = BrokenImagesPage(self.driver)
        homepage.click_broken_images()
        images = page.get_broken_images()
        print(f"Total number of images: {len(images)}")
        broken_images_count = 0
        for image in images:
            response = requests.get(image.get_attribute("src"), stream=True)
            if response.status_code != 200:
                print(image.get_attribute('outerHTML') + "is broken")
                broken_images_count += 1
        print("Total number of broken images:", broken_images_count)

        self.driver.back()

    def test_checkboxes(self):
        homepage = HomePage(self.driver)
        page = CheckboxesPage(self.driver)
        homepage.click_checkboxes()

        page.select_checkbox(1)
        assert page.get_checkbox_by_index(1).is_selected(), "First checkbox is not selected"
        page.select_checkbox(2)
        assert not page.get_checkbox_by_index(2).is_selected(), "Second checkbox is still selected"

        self.driver.back()

    def test_context_menu(self):
        homepage = HomePage(self.driver)
        basepage = BasePage(self.driver)
        page = ContextMenuPage(self.driver)
        homepage.click_context_menu()

        page.right_click_on_box()
        alert_text = basepage.get_alert_text()
        assert "You selected a context menu" in alert_text
        basepage.accept_alert()

        self.driver.back()

    def test_disappearing_elements(self):
        homepage = HomePage(self.driver)
        page = DisappearingElementsPage(self.driver)

        homepage.click_disappearing_elements()
        initial_elements_length = page.get_disappearing_elements_length()

