from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, browser):
        self.browser = browser
    
    def checkout(self):
        self.browser.find_element(By.ID, "checkout").click()
    
    def fill_info(self, first_name, last_name, postal_code):
        self.browser.find_element(By.ID, "first-name").send_keys(first_name)
        self.browser.find_element(By.ID, "last-name").send_keys(last_name)
        self.browser.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.browser.find_element(By.ID, "continue").click()
    
    def get_total(self):
        return self.browser.find_element(By.CLASS_NAME, "summary_total_label").text
