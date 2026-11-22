import pytest
from playwright.sync_api import Page, expect
from configs.settings import TEST_APP_URL

NEW_WINDOW_TEXT = "New Window"

class TestMultipleWindows2:
    def test_multiple_windows(self, page: Page):
        page.goto(TEST_APP_URL)

        page.get_by_role("link", name="Multiple Windows").click()

        click_here_link = page.get_by_role("link", name="Click here")

        with page.context.expect_page() as new_page_info:
            click_here_link.click()
        new_window = new_page_info.value

        new_window.wait_for_load_state()
        expect(new_window.locator(".example h3")).to_have_text(NEW_WINDOW_TEXT)

        print("new_window_url:", new_window.url)
        print("new_window_title:", new_window.title())



