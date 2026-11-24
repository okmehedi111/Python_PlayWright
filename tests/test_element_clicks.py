import pytest
from playwright.sync_api import Page, expect
from configs.settings import TEST_APP_URL

class TestElementClicks:
    def test_element_click(self, page: Page):
        page.goto(TEST_APP_URL)
        page.get_by_role("link", name="Context Menu").click()

        page.locator("#hot-spot").click(button="right")
