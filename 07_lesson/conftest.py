import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def firefox_browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
