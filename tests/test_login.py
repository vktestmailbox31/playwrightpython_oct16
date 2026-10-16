import os

import pytest
from playwright.sync_api import Page, expect

@pytest.mark.smoke
@pytest.mark.usefixtures("navigation")
def test_login(page: Page):
    page.get_by_role("link", name="Hello, sign in Account & Lists").click()
    page.get_by_role("textbox", name="Enter mobile number or email").click()
    page.get_by_role("textbox", name="Enter mobile number or email").fill('vktestmailbox31@gmail.com')
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill('$uFi&#ap3Wb&ALx')
    page.get_by_role("button", name="Sign in", exact=True).click()
    expect(page.locator("#nav-link-accountList-nav-line-1")).to_contain_text("Hello,")
    print("Login Successful")
