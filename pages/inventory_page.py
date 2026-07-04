"""Page object for the SauceDemo product inventory page."""

from playwright.sync_api import Page


class InventoryPage:
    """Representing (product listing) page"""

    def __init__(self, page: Page):
        self.page = page
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_product_to_cart(self, product_name: str):
        """Add a single product"""
        product_row = self.page.locator(".inventory_item", has_text=product_name)
        product_row.get_by_role("button", name="Add to cart").click()

    def go_to_cart(self):
        """Navigate to the shopping cart page"""
        self.cart_icon.click()

    def get_cart_badge_count(self) -> str:
        
        if self.cart_badge.count() == 0:
            return "0"
        return self.cart_badge.text_content()
