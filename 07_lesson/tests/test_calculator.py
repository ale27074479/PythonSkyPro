import pytest
from pages.calculator import CalculatorPage

def test_calculator(browser):
    calculator_page = CalculatorPage(browser)
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    calculator_page.set_delay("45")
    calculator_page.click_button("7")
    calculator_page.click_button("+")
    calculator_page.click_button("8")
    calculator_page.click_button("=")
    
    result = calculator_page.get_result()
    assert "15" in result, f"Expected 15, but got {result}"
