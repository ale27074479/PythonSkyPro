import pytest
import requests
import allure
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://yougile.com/api-v2"


@allure.feature("API тесты для работы с проектами Yougile")
class TestProjectsAPI:
    
    @allure.story("Позитивные тесты")
    @allure.title("Создание проекта (позитивный)")
    def test_create_project_positive(self, auth_headers):
        """Тест успешного создания проекта."""
        with allure.step("Подготовка тестовых данных"):
            project_data = {
                "title": "New Test Project",
                "users": {}
            }
        
        with allure.step("Отправка POST запроса для создания проекта"):
            response = requests.post(
                f"{BASE_URL}/projects",
                headers=auth_headers,
                json=project_data
            )
            allure.attach(
                str(response.json()),
                name="Response",
                attachment_type=allure.attachment_type.JSON
            )
        
        with allure.step("Проверка ответа"):
            assert response.status_code in [201, 200], \
                f"Неожиданный статус код: {response.status_code}"
            response_data = response.json()
            assert "id" in response_data, "Ответ должен содержать ID проекта"
            
            if "title" in response_data:
                assert response_data["title"] == project_data["title"], \
                    "Название проекта не совпадает"
        
        with allure.step("Удаление созданного проекта"):
            project_id = response_data["id"]
            requests.delete(
                f"{BASE_URL}/projects/{project_id}",
                headers=auth_headers
            )

    @allure.story("Позитивные тесты")
    @allure.title("Получение информации о проекте (позитивный)")
    def test_get_project_positive(self, auth_headers, test_project):
        """Тест успешного получения информации о проекте."""
        with allure.step(f"Отправка GET запроса для проекта {test_project}"):
            response = requests.get(
                f"{BASE_URL}/projects/{test_project}",
                headers=auth_headers
            )
            allure.attach(
                str(response.json()),
                name="Response",
                attachment_type=allure.attachment_type.JSON
            )
        
        with allure.step("Проверка ответа"):
            assert response.status_code == 200, \
                f"Неожиданный статус код: {response.status_code}"
            assert "id" in response.json(), "Ответ должен содержать ID проекта"
            assert response.json()["id"] == test_project, "ID проекта не совпадает"

    @allure.story("Позитивные тесты")
    @allure.title("Обновление проекта (позитивный)")
    def test_update_project_positive(self, auth_headers, test_project):
        """Тест успешного обновления проекта."""
        with allure.step("Подготовка данных для обновления"):
            updated_data = {
                "title": "Updated Test Project",
                "users": {}
            }
        
        with allure.step(f"Отправка PUT запроса для проекта {test_project}"):
            response = requests.put(
                f"{BASE_URL}/projects/{test_project}",
                headers=auth_headers,
                json=updated_data
            )
            allure.attach(
                str(response.json()),
                name="Response",
                attachment_type=allure.attachment_type.JSON
            )
        
        with allure.step("Проверка ответа"):
            assert response.status_code == 200, \
                f"Неожиданный статус код: {response.status_code}"
            response_data = response.json()
            if "title" in response_data:
                assert response_data["title"] == updated_data["title"], \
                    "Название проекта не обновилось"

    @allure.story("Негативные тесты")
    @allure.title("Создание проекта без названия (негативный)")
    def test_create_project_negative_missing_title(self, auth_headers):
        """Тест создания проекта без названия."""
        with allure.step("Подготовка невалидных данных"):
            project_data = {"users": {}}
        
        with allure.step("Отправка POST запроса с невалидными данными"):
            response = requests.post(
                f"{BASE_URL}/projects",
                headers=auth_headers,
                json=project_data
            )
            allure.attach(
                str(response.json()),
                name="Response",
                attachment_type=allure.attachment_type.JSON
            )
        
        with allure.step("Проверка ошибки"):
            assert response.status_code == 400, \
                f"Ожидался код 400, получен {response.status_code}"

    @allure.story("Негативные тесты")
    @allure.title("Получение несуществующего проекта (негативный)")
    def test_get_project_negative_invalid_id(self, auth_headers):
        """Тест получения несуществующего проекта."""
        with allure.step("Подготовка невалидного ID проекта"):
            invalid_id = "invalid-project-id"
        
        with allure.step(f"Отправка GET запроса для несуществующего проекта {invalid_id}"):
            response = requests.get(
                f"{BASE_URL}/projects/{invalid_id}",
                headers=auth_headers
            )
            allure.attach(
                str(response.json()),
                name="Response",
                attachment_type=allure.attachment_type.JSON
            )
        
        with allure.step("Проверка ошибки"):
            assert response.status_code in [400, 404], \
                f"Ожидался код 400/404, получен {response.status_code}"

    @allure.story("Негативные тесты")
    @allure.title("Обновление проекта с невалидным пользователем (негативный)")
    def test_update_project_negative_invalid_user(self, auth_headers, test_project):
        """Тест обновления проекта с невалидным пользователем."""
        with allure.step("Подготовка невалидных данных пользователя"):
            updated_data = {
                "title": "Updated Test Project",
                "users": {"invalid-user-id": "admin"}
            }
        
        with allure.step(f"Отправка PUT запроса с невалидными данными для проекта {test_project}"):
            response = requests.put(
                f"{BASE_URL}/projects/{test_project}",
                headers=auth_headers,
                json=updated_data
            )
            allure.attach(
                str(response.json()),
                name="Response",
                attachment_type=allure.attachment_type.JSON
            )
        
        with allure.step("Проверка ошибки"):
            assert response.status_code in [400, 404], \
                f"Ожидался код 400, получен {response.status_code}"
