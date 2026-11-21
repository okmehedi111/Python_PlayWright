import pytest
from playwright.sync_api import Page
from configs.settings import TEST_APP_URL

def test_iframe(page: Page):
    page.goto(TEST_APP_URL)

    page.get_by_text("Frames", exact= True).click()
    page.get_by_text("iFrame", exact= True).click()

    iframe = page.frame_locator("#mce_0_ifr")

    iframe.locator("body").fill("Learning Playwright with python")
    text = iframe.locator("body").inner_text()

    print("body text:",text)

    assert text == "Learning Playwright with python"




