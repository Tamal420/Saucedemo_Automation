"""Page objects for the three-step SauceDemo checkout flow."""

from playwright.sync_api import Page


class CheckoutInfoPage:
    """Step one: customer enters first name, last name, and postal code."""

    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.error_message = page.locator("[data-test='error']")

    def fill_information(self, first_name: str = "", last_name: str = "", postal_code: str = ""):
        """Fill only the fields that are given, useful for negative testing."""
        if first_name:
            self.first_name_input.fill(first_name)
        if last_name:
            self.last_name_input.fill(last_name)
        if postal_code:
            self.postal_code_input.fill(postal_code)

    def click_continue(self):
        self.continue_button.click()


class CheckoutOverviewPage:
    """Step two: customer reviews the order summary before finishing."""

    def __init__(self, page: Page):
        self.page = page
        self.finish_button = page.locator("#finish")

    def finish_order(self):
        self.finish_button.click()


class CheckoutCompletePage:
    """Step three: confirmation screen shown after a successful order."""

    def __init__(self, page: Page):
        self.page = page
        self.complete_header = page.locator(".complete-header")

    def get_confirmation_message(self) -> str:
        return self.complete_header.text_content()
