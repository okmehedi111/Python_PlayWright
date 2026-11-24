import pytest
from playwright.sync_api import Page, expect
from configs.settings import TEST_APP_URL
INPUT_TEXT = "test"

class TestExersise:
    def iframe(self, page: Page):
        page.goto(TEST_APP_URL)
        page.get_by_role("link", name="Frames").click()
        page.get_by_role("link", name="iFrame").click()

        iframe = page.locator("#mce_0_ifr")
        iframe.locator("body").fill(INPUT_TEXT)
        text = iframe.locator("body").inner_text()
        assert INPUT_TEXT == text



