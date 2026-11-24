import pytest
from playwright.sync_api import Page, expect
from configs.settings import TEST_APP_URL
INPUT_MGS = "Hello"


class TestAlertHandilingInput:
    def test_alert_handiling_input(self, page: Page):
        page.goto(TEST_APP_URL)

        page.get_by_role("link", name="JavaScript Alerts").click()

        page.on("dialog", lambda dialog: dialog.accept(INPUT_MGS))
        page.get_by_role("button", name="Click for JS Prompt").click()

        expect(page.locator("#result")).to_contain_text(INPUT_MGS)






