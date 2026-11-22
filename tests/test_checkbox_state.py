import pytest
from playwright.sync_api import Page, expect
from configs.settings import TEST_APP_URL

class TestCheckboxState:
    def test_checkbox_state(self, page: Page):
        page.goto(TEST_APP_URL)
        page.get_by_role("link", name="Checkboxes").click()
        
        checkboxes = page.locator("input[type = 'checkbox']")
        first_checkbox = checkboxes.nth(0)
        second_checkbox = checkboxes.nth(1)

        expect(first_checkbox).not_to_be_checked()
        expect(second_checkbox).to_be_checked()

        first_checkbox.check()
        second_checkbox.uncheck()

        expect(first_checkbox).to_be_checked()
        expect(second_checkbox).not_to_be_checked()

