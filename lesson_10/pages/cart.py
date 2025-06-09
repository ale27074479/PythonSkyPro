from selenium.webdriver.common.by import By
import allure


class CartPage:
    """Page Object для корзины покупок."""

    def __init__(self, browser):
        """Инициализация страницы корзины.
        
        Args:
            browser: WebDriver - экземпляр веб-драйвера
        """
        self.browser = browser
    
    @allure.step("Перейти к оформлению заказа")
    def checkout(self) -> None:
        """Нажимает кнопку оформления заказа."""
        self.browser.find_element(By.ID, "checkout").click()
    
    @allure.step("Заполнить информацию: {first_name} {last_name}, {postal_code}")
    def fill_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        """Заполняет информацию для оформления заказа.
        
        Args:
            first_name: str - имя покупателя
            last_name: str - фамилия покупателя
            postal_code: str - почтовый индекс
        """
        self.browser.find_element(By.ID, "first-name").send_keys(first_name)
        self.browser.find_element(By.ID, "last-name").send_keys(last_name)
        self.browser.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.browser.find_element(By.ID, "continue").click()
    
    @allure.step("Получить итоговую сумму заказа")
    def get_total(self) -> str:
        """Возвращает итоговую сумму заказа.
        
        Returns:
            str: текст с итоговой суммой
        """
        return self.browser.find_element(By.CLASS_NAME, "summary_total_label").text
