import pytest
from playwright.sync_api import Page, expect
from configs.settings import TEST_APP_URL

FAILURE_LOGIN_MGS = "Your username is invalid!"

class TestFailureLogin:
    def test_failure_login(self, page: Page):
        page.goto(TEST_APP_URL.rstrip("/") + "/login")

        expect(page.get_by_label("Username")).to_be_visible()

        page.get_by_role("button", name="Login").click()

        message = page.get_by_text("invalid").inner_text().lower()

        assert FAILURE_LOGIN_MGS.lower() in message


