import pytest
from playwright.sync_api import Playwright, expect, Page
from configs.settings import TEST_APP_URL

TEST_NAME = "Smith"

class TestDataTables:
    def test_data_tables(self, page: Page):
        page.goto(TEST_APP_URL)
        page.get_by_role("link", name="Sortable Data Tables").click()

        rows = page.locator("#table1 tbody tr")
        rows_count = rows.count()
        print(f"There are {rows_count} rows")

        first_row = rows.nth(0)
        print(f"First row is {first_row}")
        expect(first_row).to_contain_text(TEST_NAME)

