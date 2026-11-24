import pytest
from playwright.sync_api import Page
from configs.settings import TEST_APP_URL

def test_navigation(page: Page):
    page.goto(TEST_APP_URL)
    print("navigation url:", page.url)

    page.goto(TEST_APP_URL.rstrip("/") + "/two_factor")
    print("Login Page Url:", page.url)

    page.go_back()
    print("home page url:", page.url)

    page.go_forward()
    print("login page url:", page.url)
