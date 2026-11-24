import pytest
from playwright.sync_api import Page, expect
from configs.settings import TEST_APP_URL

class TestCookies:
    def test_cookies(self, page: Page):
        page.goto(TEST_APP_URL)

        context = page.context
        context.add_cookies([
            {
                "name": "testKey",
                "value": "testValue",
                "url": TEST_APP_URL
            }
        ])
        cookies = context.cookies()
        test_cookie = next(cookie for cookie in cookies if cookie["name"] == "testKey")
        assert test_cookie["value"] == "testValue"

        context.clear_cookies()
        cookies = context.cookies()
        assert not any(cookie for cookie in cookies if cookie["name"] == "testKey")




