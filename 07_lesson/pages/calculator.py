from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, browser):
        self.browser = browser
    
    def set_delay(self, delay):
        delay_field = self.browser.find_element(By.CSS_SELECTOR, "#delay")
        delay_field.clear()
        delay_field.send_keys(delay)
    
    def click_button(self, button_text):
        button = self.browser.find_element(By.XPATH, f"//span[text()='{button_text}']")
        button.click()
    
    def get_result(self):
        result = WebDriverWait(self.browser, 46).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )
        return self.browser.find_element(By.CSS_SELECTOR, ".screen").text
