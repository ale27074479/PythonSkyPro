import pytest
import allure
from pages.login import LoginPage
from pages.main import MainPage
from pages.cart import CartPage


@allure.feature("Тестирование интернет-магазина")
@allure.severity(allure.severity_level.BLOCKER)
class TestShop:
    """Тесты для интернет-магазина."""

    @allure.title("Проверка итоговой суммы заказа")
    @allure.description("Тест проверяет корректность расчета итоговой суммы заказа")
    def test_shop_total(self, firefox_browser):
        """Тест проверки итоговой суммы заказа."""
        with allure.step("Авторизация пользователя"):
            login_page = LoginPage(firefox_browser)
            login_page.login("standard_user", "secret_sauce")
        
        with allure.step("Добавление товаров в корзину"):
            main_page = MainPage(firefox_browser)
            main_page.add_to_cart(
                "Sauce Labs Backpack",
                "Sauce Labs Bolt T-Shirt",
                "Sauce Labs Onesie"
            )
            main_page.go_to_cart()
        
        with allure.step("Оформление заказа"):
            cart_page = CartPage(firefox_browser)
            cart_page.checkout()
            cart_page.fill_info("John", "Doe", "12345")
        
        with allure.step("Проверка итоговой суммы"):
            total = cart_page.get_total()
            assert total == "Total: $58.29", f"Expected $58.29, but got {total}"
