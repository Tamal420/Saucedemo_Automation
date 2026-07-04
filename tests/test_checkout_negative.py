"""Negative scenario: checkout must be blocked when required information is missing."""

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutInfoPage

VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"
PRODUCT_NAME = "Sauce Labs Backpack"


class TestCheckoutNegative:
    def test_checkout_blocked_when_last_name_is_missing(self, page):
        # Arrange: log in and get a product into the cart
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        inventory_page = InventoryPage(page)
        inventory_page.add_product_to_cart(PRODUCT_NAME)
        inventory_page.go_to_cart()

        cart_page = CartPage(page)
        cart_page.go_to_checkout()

        # Act: submit the checkout form without a last name
        checkout_info_page = CheckoutInfoPage(page)
        checkout_info_page.fill_information(first_name="Tamal", postal_code="1207")
        checkout_info_page.click_continue()

        # Assert: the app must reject the submission with a clear error
        error_text = checkout_info_page.error_message.text_content()
        assert error_text == "Error: Last Name is required", (
            f"Unexpected error message: '{error_text}'"
        )

        assert page.url.endswith("checkout-step-one.html"), (
            "User was allowed to proceed past checkout despite missing required field"
        )
