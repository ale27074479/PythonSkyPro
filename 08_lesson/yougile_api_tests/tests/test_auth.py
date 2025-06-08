import pytest
from api.auth import AuthAPI


class TestAuth:
    def test_create_auth_key_success(self, auth_api):
        """Позитивный тест получения токена"""
        response = auth_api.create_auth_key()
        assert response.status_code in [200, 201], (
            f"Expected 200 or 201, got {response.status_code}. Response: {response.text}"
        )
        assert 'token' in response.json()

    def test_create_auth_key_invalid_credentials(self, auth_api):
        """Негативный тест с неверными учетными данными"""
        response = auth_api.create_auth_key("wrong@email.com", "wrongpassword")
        assert response.status_code in [400, 401]
