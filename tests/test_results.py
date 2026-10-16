import re
import pytest
from playwright.sync_api import Page, expect
   
@pytest.mark.smoke
@pytest.mark.usefixtures("navigation")
def test_resultsScreenUI(page: Page , navigation):    
    page.get_by_role("searchbox", name="Search Amazon.in").click()
    page.get_by_role("searchbox", name="Search Amazon.in").fill("Iphone")
    page.get_by_role("searchbox", name="Search Amazon.in").press("Enter")
    expect(page.get_by_role("heading", name="Results", exact=True)).to_be_visible()
    expect(page.get_by_text("Eligible for Free Delivery")).to_be_visible()
    
@pytest.mark.smoke
@pytest.mark.usefixtures("navigation")    
def test_Cart_value(page: Page , navigation , slow_mo=3000):
    page.get_by_role("searchbox", name="Search Amazon.in").click()
    page.get_by_role("searchbox", name="Search Amazon.in").fill("iphone")
    page.get_by_role("searchbox", name="Search Amazon.in").press("Enter")
    page.locator("#a-autoid-3").get_by_role("button", name="Add to cart").click()
    expect(page.locator("#nav-cart-count")).to_contain_text("1")