import pytest

@pytest.fixture
def navigation(page):
    page.goto("https://www.amazon.in/")
    
    #  browser = playwright.chromium.launch(headless=False)
    #     context = browser.new_context()
    #     page = context.new_page()
    #     page.goto("https://www.amazon.in/")
