from selenium.webdriver.common.by import By
import allure


class MainPage:
    """Page Object для главной страницы магазина."""

    def __init__(self, browser):
        """Инициализация главной страницы.
        
        Args:
            browser: WebDriver - экземпляр веб-драйвера
        """
        self.browser = browser
    
    @allure.step("Добавить товары в корзину: {items}")
    def add_to_cart(self, *items: str) -> None:
        """Добавляет указанные товары в корзину.
        
        Args:
            *items: str - названия товаров для добавления
        """
        for item in items:
            self.browser.find_element(
                By.XPATH, 
                f"//div[text()='{item}']/ancestor::div[@class='inventory_item']//button"
            ).click()
    
    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """Переходит на страницу корзины."""
        self.browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
