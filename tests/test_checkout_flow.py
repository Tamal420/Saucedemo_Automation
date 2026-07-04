

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutInfoPage, CheckoutOverviewPage, CheckoutCompletePage

VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"
PRODUCT_NAME = "Sauce Labs Backpack"


class TestCheckoutFlow:
    def test_user_can_complete_checkout_successfully(self, page):
        # Step 1: Log in with valid credentials
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        assert page.url.endswith("inventory.html"), (
            "Login did not redirect to the inventory page"
        )

        # Step 2: Add a product to the cart
        inventory_page = InventoryPage(page)
        inventory_page.add_product_to_cart(PRODUCT_NAME)

        assert inventory_page.get_cart_badge_count() == "1", (
            "Cart badge did not update after adding a product"
        )

        # Step 3: Go to the cart and verify its contents
        inventory_page.go_to_cart()
        cart_page = CartPage(page)

        assert cart_page.get_item_count() == 1, (
            "Cart does not contain the expected number of items"
        )

        # Step 4: Proceed to checkout and fill in customer information
        cart_page.go_to_checkout()
        checkout_info_page = CheckoutInfoPage(page)
        checkout_info_page.fill_information(
            first_name="Tamal", last_name="Hasan", postal_code="1207"
        )
        checkout_info_page.click_continue()

        assert page.url.endswith("checkout-step-two.html"), (
            "Did not proceed to the order overview step"
        )

        # Step 5: Finish the order
        checkout_overview_page = CheckoutOverviewPage(page)
        checkout_overview_page.finish_order()

        # Step 6: Verify the order confirmation message
        checkout_complete_page = CheckoutCompletePage(page)
        confirmation_message = checkout_complete_page.get_confirmation_message()

        assert confirmation_message == "Thank you for your order!", (
            f"Unexpected confirmation message: '{confirmation_message}'"
        )
