import pytest
from api.auth import AuthAPI
from api.projects import ProjectsAPI

@pytest.fixture
def auth_api():
    return AuthAPI()

@pytest.fixture
def projects_api():
    return ProjectsAPI()

@pytest.fixture
def valid_token(auth_api):
    response = auth_api.create_auth_key()
    assert response.status_code == 200, "Failed to get auth token"
    return response.json()['token']

@pytest.fixture
def company_id(auth_api, valid_token):
    response = auth_api.get_companies_list(valid_token)
    assert response.status_code == 200, "Failed to get companies list"
    companies = response.json()
    return companies[0]['id'] if companies else None

@pytest.fixture
def created_project(projects_api, valid_token, company_id):
    response = projects_api.create_project(
        token=valid_token,
        company_id=company_id,
        title="Test Project"
    )
    assert response.status_code == 201, "Failed to create test project"
    project_id = response.json()['id']
    yield project_id
    # Cleanup
    projects_api.delete_project(valid_token, project_id)

