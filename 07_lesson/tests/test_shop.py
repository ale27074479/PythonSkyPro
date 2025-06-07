import pytest
from pages.login import LoginPage
from pages.main import MainPage
from pages.cart import CartPage

def test_shop_total(firefox_browser):
    # Login
    login_page = LoginPage(firefox_browser)
    login_page.login("standard_user", "secret_sauce")
    
    # Add items to cart
    main_page = MainPage(firefox_browser)
    main_page.add_to_cart(
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    )
    main_page.go_to_cart()
    
    # Checkout
    cart_page = CartPage(firefox_browser)
    cart_page.checkout()
    cart_page.fill_info("John", "Doe", "12345")
    
    # Verify total
    total = cart_page.get_total()
    assert total == "Total: $58.29", f"Expected $58.29, but got {total}"
