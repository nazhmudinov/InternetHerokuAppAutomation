import pytest

from pages.AddRemoveElementsPage import AddRemoveElementsPage
from pages.BasePage import BasePage


class TestE2e(BasePage):
    def test_add_remove_elements(self):
        page = AddRemoveElementsPage(self.driver)
        page.click_add_element()