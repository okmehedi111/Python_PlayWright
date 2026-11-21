import pytest
from playwright.sync_api import Page
from configs.settings import TEST_APP_URL

def test_open_website(page: Page):

    page.goto(TEST_APP_URL)

    print("before refresh", page.url)

    page.reload()

    print("after refresh", page.url)
    print("Page Title:", page.title())

def test_refresh_page(page: Page):
    page.goto(TEST_APP_URL)
    print("before refresh", page.url)
    page.reload()
    print("after refresh", page.url)
    print("Page Title:", page.title())


def test_navigation_back(page: Page):
    page.goto(TEST_APP_URL)
    print("homepage url:", page.url)

    page.goto(TEST_APP_URL.rstrip("/") + "/two_factor")
    print("login_page url:", page.url)

    page.go_back()
    print("back url:", page.url)
    print("Page Title:", page.title())

    page.go_forward()
    print("forward url:", page.url)

