import pytest
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://yougile.com/api-v2"
API_KEY = os.getenv("YOUGILE_API_KEY")


@pytest.fixture
def auth_headers():
    """Фикстура для заголовков авторизации API Yougile."""
    if not API_KEY:
        pytest.skip("API key not provided")
    return {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }


@pytest.fixture
def test_project(auth_headers):
    """Фикстура для создания временного тестового проекта.
    
    Проект автоматически удаляется после завершения теста.
    """
    project_data = {
        "title": "Test Project Fixture",
        "users": {}
    }
    response = requests.post(
        f"{BASE_URL}/projects",
        headers=auth_headers,
        json=project_data
    )
    assert response.status_code in [200, 201], "Не удалось создать тестовый проект"
    project_id = response.json()["id"]
    
    yield project_id  # Возвращает ID проекта тесту
    
    # После теста проект удаляется
    requests.delete(
        f"{BASE_URL}/projects/{project_id}",
        headers=auth_headers
    )
