import os
import shutil
import pytest
from playwright.sync_api import Page, expect
from configs.settings import TEST_APP_URL

DOWNLOAD_DIR = "./downloads"
TEST_FILE = "some-file.txt"

class TestFileDownload2:
    def test_file_download2(self, page: Page):
        if not os.path.exists(DOWNLOAD_DIR):
            os.makedirs(DOWNLOAD_DIR)

        page.goto(TEST_APP_URL)
        page.get_by_role("link", name= "File Download", exact= True).click()
        expect(page.locator(".example h3")).to_have_text("File Downloader")

        file_link = page.get_by_role("link", name= TEST_FILE, exact= True)
        downloaded_file_path = os.path.join(DOWNLOAD_DIR, TEST_FILE)

        with page.expect_download() as download_info:
            file_link.click()
        download = download_info.value
        download.save_as(downloaded_file_path)

        assert os.path.exists(downloaded_file_path), f'{downloaded_file_path} does not exist'

        shutil.rmtree(DOWNLOAD_DIR)

