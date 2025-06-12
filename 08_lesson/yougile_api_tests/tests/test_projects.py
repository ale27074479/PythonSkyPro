import pytest

def test_create_project_positive(valid_token, company_id, projects_api):
    """Позитивный тест создания проекта"""
    response = projects_api.create_project(
        token=valid_token,
        company_id=company_id,
        title="New Project"
    )
    assert response.status_code == 201
    assert 'id' in response.json()
    assert response.json()['title'] == "New Project"

def test_create_project_negative(company_id, projects_api):
    """Негативный тест создания проекта (неверный токен)"""
    response = projects_api.create_project(
        token="invalid_token",
        company_id=company_id,
        title="New Project"
    )
    assert response.status_code == 401

def test_create_project_without_company_id(valid_token, projects_api):
    """Негативный тест создания проекта (без company_id)"""
    response = projects_api.create_project(
        token=valid_token,
        company_id="",
        title="New Project"
    )
    assert response.status_code in [400, 422]

def test_get_project_positive(valid_token, projects_api, created_project):
    """Позитивный тест получения проекта"""
    response = projects_api.get_project(valid_token, created_project)
    assert response.status_code == 200
    assert response.json()['id'] == created_project

def test_get_project_negative(projects_api, created_project):
    """Негативный тест получения проекта"""
    response = projects_api.get_project("invalid_token", created_project)
    assert response.status_code == 401

def test_update_project_positive(valid_token, projects_api, created_project):
    """Позитивный тест обновления проекта"""
    response = projects_api.update_project(
        token=valid_token,
        project_id=created_project,
        title="Updated Title"
    )
    assert response.status_code == 200
    assert response.json()['title'] == "Updated Title"

def test_update_project_negative(projects_api, created_project):
    """Негативный тест обновления проекта"""
    response = projects_api.update_project(
        token="invalid_token",
        project_id=created_project,
        title="Updated Title"
    )
    assert response.status_code == 401

def test_delete_project_positive(valid_token, company_id, projects_api):
    """Позитивный тест удаления проекта"""
    # Создаем временный проект для удаления
    create_response = projects_api.create_project(
        token=valid_token,
        company_id=company_id,
        title="Temp Project"
    )
    project_id = create_response.json()['id']
    
    # Удаляем проект
    delete_response = projects_api.delete_project(valid_token, project_id)
    assert delete_response.status_code in [200, 204]
    
    # Проверяем, что проект действительно удален
    get_response = projects_api.get_project(valid_token, project_id)
    assert get_response.status_code == 404

def test_delete_project_negative(projects_api, created_project):
    """Негативный тест удаления проекта"""
    response = projects_api.delete_project("invalid_token", created_project)
    assert response.status_code == 401
