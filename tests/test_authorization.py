import pytest
from playwright.sync_api import Page

from page.authorization import authorizationPage
from utils.jsonhandling import load_test_data


@pytest.mark.smoke
@pytest.mark.usefixtures("navigation")
def test_invalid_username_shows_error(page: Page) -> None:
    authorization_page = authorizationPage(page)
    authorization_page.sign_in_button()
    authorization_page.enter_login_id("invalid-user-name")
    authorization_page.click_continue_button()
    authorization_page.validate_login_email()


@pytest.mark.smoke
@pytest.mark.usefixtures("navigation")
def test_valid_login(page: Page , navigation):
    test_data = load_test_data()
    credentials = test_data["positiveCreds"]
    username = credentials["username"]
    password = credentials["password"]
    expected_name = test_data["expected_name"]
    
    authorization_page = authorizationPage(page)
    authorization_page.sign_in_button()
    authorization_page.enter_login_id(username)
    authorization_page.click_continue_button()
    authorization_page.enter_password(password)
    authorization_page.submit_sign_in()
    authorization_page.validate_successful_sign_in(expected_name)
