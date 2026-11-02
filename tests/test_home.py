import pytest
from playwright.sync_api import Page, expect
from page.home import HomePage

@pytest.mark.smoke
@pytest.mark.usefixtures("navigation")
def test_homescreenui(page: Page , navigation):
    homepageconst = HomePage(page)
    homepageconst.validateSearchedVisibilities()
    homepageconst.validateCartTextVisibiblities()
    homepageconst.ValidatingSearchBox()
