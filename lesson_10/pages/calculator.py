from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:
    """Page Object для калькулятора с задержкой."""

    def __init__(self, browser):
        """Инициализация страницы калькулятора.
        
        Args:
            browser: WebDriver - экземпляр веб-драйвера
        """
        self.browser = browser
    
    @allure.step("Установить задержку в {delay} секунд")
    def set_delay(self, delay: str) -> None:
        """Устанавливает значение задержки вычислений.
        
        Args:
            delay: str - значение задержки в секундах
        """
        delay_field = self.browser.find_element(By.CSS_SELECTOR, "#delay")
        delay_field.clear()
        delay_field.send_keys(delay)
    
    @allure.step("Нажать кнопку '{button_text}'")
    def click_button(self, button_text: str) -> None:
        """Нажимает кнопку с указанным текстом.
        
        Args:
            button_text: str - текст на кнопке
        """
        button = self.browser.find_element(By.XPATH, f"//span[text()='{button_text}']")
        button.click()
    
    @allure.step("Получить результат вычислений")
    def get_result(self) -> str:
        """Ожидает и возвращает результат вычислений.
        
        Returns:
            str: текст результата на экране калькулятора
        """
        result = WebDriverWait(self.browser, 46).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )
        return self.browser.find_element(By.CSS_SELECTOR, ".screen").text
