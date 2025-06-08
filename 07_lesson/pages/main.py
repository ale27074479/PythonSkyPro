from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, browser):
        self.browser = browser
    
    def add_to_cart(self, *items):
        for item in items:
            self.browser.find_element(By.XPATH, f"//div[text()='{item}']/ancestor::div[@class='inventory_item']//button").click()
    
    def go_to_cart(self):
        self.browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
