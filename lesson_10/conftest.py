import pytest
from selenium import webdriver
import allure


@pytest.fixture
def browser():
    """Фикстура для создания и закрытия Chrome браузера."""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def firefox_browser():
    """Фикстура для создания и закрытия Firefox браузера."""
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
