import pytest
import logging
from api.auth import AuthAPI

logging.basicConfig(level=logging.DEBUG)

class TestAuth:
    def test_create_auth_key_success(self, auth_api):
        """Позитивный тест получения токена"""
        response = auth_api.create_auth_key()
        assert response.status_code == 200
        assert 'token' in response.json()

    def test_get_companies_list_success(self, auth_api, valid_token):
        """Позитивный тест получения списка компаний"""
        response = auth_api.get_companies_list(valid_token)
        assert response.status_code == 200
        assert isinstance(response.json(), list)

def test_create_auth_key_invalid_credentials():
    """Негативный тест с неверными учетными данными"""
    invalid_api = AuthAPI()
    invalid_api.login = "invalid@email.com"
    invalid_api.password = "wrongpassword"
    
    response = invalid_api.create_auth_key()
    assert response.status_code == 401
