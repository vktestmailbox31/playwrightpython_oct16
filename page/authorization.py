from playwright.sync_api import Locator, Page, expect


class authorizationPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.signinbutton = page.get_by_role(
            "link", name="Hello, sign in Account & Lists"
        )
        self.emailId_txt_bar = page.get_by_role(
            "textbox", name="Enter mobile number or email"
        )
        self.continue_button = page.get_by_role("button", name="Continue")
        self.password_link = page.get_by_role("link", name="Enter your password")
        self.password_textbox = page.get_by_role("textbox", name="Password")
        self.submit_sign_in_button = page.get_by_role(
            "button", name="Sign in", exact=True
        )
        self.invalid_alert: Locator = page.get_by_role("alert")

    def sign_in_button(self) -> None:
        self.signinbutton.click()

    def enter_login_id(self, email: str) -> None:
        self.emailId_txt_bar.fill(email)

    def click_continue_button(self) -> None:
        self.continue_button.click()

    def enter_password(self, password: str) -> None:
        self.password_link.click()
        self.password_textbox.fill(password)

    def submit_sign_in(self) -> None:
        self.submit_sign_in_button.click()

    def validate_successful_sign_in(self, expected_name: str) -> None:
        expect(
            self.page.locator("#nav-link-accountList-nav-line-1")
        ).to_contain_text(f"Hello, {expected_name}")

    def validate_login_email(self) -> None:
        expect(self.invalid_alert).to_have_text("Invalid email address")
