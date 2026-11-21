import pytest
from playwright.sync_api import Page, expect
from configs.settings import TEST_APP_URL

CANCEL_ALERT_MSG = "You clicked: Cancel"

class TestAlertHandilingDismiss:
    def test_alert_handiling_dismiss(self, page: Page):
        page.goto(TEST_APP_URL)

        page.get_by_role("link", name="JavaScript Alerts").click()

        page.on("dialog", lambda dialog: dialog.dismiss())
        page.get_by_role("button", name="Click for JS Confirm").click()

        expect(page.locator("#result")).to_have_text(CANCEL_ALERT_MSG)

