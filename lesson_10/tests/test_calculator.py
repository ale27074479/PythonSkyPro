import pytest
import allure
from pages.calculator import CalculatorPage


@allure.feature("Тестирование калькулятора")
@allure.severity(allure.severity_level.CRITICAL)
class TestCalculator:
    """Тесты для калькулятора с задержкой."""

    @allure.title("Проверка работы калькулятора с задержкой")
    @allure.description("Тест проверяет корректность вычислений калькулятора с установленной задержкой")
    def test_calculator(self, browser):
        """Тест работы калькулятора с задержкой."""
        calculator_page = CalculatorPage(browser)
        browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        
        with allure.step("Установить задержку и выполнить вычисления"):
            calculator_page.set_delay("45")
            calculator_page.click_button("7")
            calculator_page.click_button("+")
            calculator_page.click_button("8")
            calculator_page.click_button("=")
        
        with allure.step("Проверить результат вычислений"):
            result = calculator_page.get_result()
            assert "15" in result, f"Expected 15, but got {result}"
