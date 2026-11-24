import pytest
from playwright.sync_api import Page, expect
from configs.settings import TEST_APP_URL

class TestRelativeLocators:
    def test_relative_locator(self, page: Page):
        page.goto(TEST_APP_URL.rstrip("/") + "/login")
        username_input = page.locator("xpath=//label[@for='username']/following-sibling::input")
        expect(username_input).to_be_visible()

        password_input = page.locator("xpath=//label[@for='password']/following-sibling::input")
        expect(password_input).to_be_visible()

        #part-2
        username_parent = page.locator("xpath=//label[@for='username']/parent::div")
        expect(username_parent).to_be_visible()
        username_ancestor = page.locator("xpath=//label[@for='username']/ancestor::form")
        expect(username_ancestor).to_be_visible()
        password_previous = page.locator("xpath=//input[@name='password']/preceding-sibling::label")
        expect(password_previous).to_be_visible()

        #part-3
        username_box = username_input.bounding_box()
        password_box = password_input.bounding_box()

        assert username_box["y"] < password_box["y"],"Username input is not above Password input"



