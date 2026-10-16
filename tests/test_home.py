import pytest
from playwright.sync_api import Page, expect

@pytest.mark.smoke
@pytest.mark.usefixtures("navigation")
def test_homescreenui(page: Page , navigation):
    expect(page.get_by_role("link", name="Amazon.in")).to_be_visible()
    expect(page.get_by_role("searchbox", name="Search Amazon.in")).to_be_visible()
    expect(page.get_by_role("link", name="items in cart")).to_be_visible()