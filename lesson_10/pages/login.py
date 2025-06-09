from selenium.webdriver.common.by import By
import allure


class LoginPage:
    """Page Object для страницы авторизации."""

    def __init__(self, browser):
        """Инициализация страницы авторизации.
        
        Args:
            browser: WebDriver - экземпляр веб-драйвера
        """
        self.browser = browser
        self.browser.get("https://www.saucedemo.com/")
    
    @allure.step("Авторизоваться как {username}")
    def login(self, username: str, password: str) -> None:
        """Выполняет авторизацию пользователя.
        
        Args:
            username: str - имя пользователя
            password: str - пароль пользователя
        """
        self.browser.find_element(By.ID, "user-name").send_keys(username)
        self.browser.find_element(By.ID, "password").send_keys(password)
        self.browser.find_element(By.ID, "login-button").click()
