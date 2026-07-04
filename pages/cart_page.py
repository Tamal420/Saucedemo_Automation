"""Page object for the SauceDemo shopping cart page."""

from playwright.sync_api import Page


class CartPage:
    """Represents the shopping cart page."""

    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator("#checkout")

    def get_item_count(self) -> int:
        """Return how many items are currently in the cart."""
        return self.cart_items.count()

    def go_to_checkout(self):
        """Proceed from the cart to the checkout information step."""
        self.checkout_button.click()
