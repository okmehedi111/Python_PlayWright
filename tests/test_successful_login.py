import pytest
from playwright.sync_api import Page, expect
from configs.settings import TEST_APP_URL

SUCCESS_LOGIN_MGS = "You logged into a secure area!"

class Test_succesful_login:
    def test_succesful_login(self, page: Page):
        page.goto(TEST_APP_URL.rstrip("/") + "/login")
        expect(page.get_by_label("Username")).to_be_visible()

        page.get_by_label("Username").fill("tomsmith")
        page.get_by_label("Password").fill("SuperSecretPassword!")
        page.get_by_role("button", name="login").click()
        expect(page.locator("#flash")).to_contain_text(SUCCESS_LOGIN_MGS)



