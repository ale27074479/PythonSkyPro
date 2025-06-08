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
def valid_token_and_company(auth_api):
    # Получаем токен
    token_response = auth_api.create_auth_key()
    
    if token_response.status_code not in [200, 201]:
        pytest.fail(
            f"Failed to get auth token. Status: {token_response.status_code}. "
            f"Response: {token_response.text}"
        )
    
    token = token_response.json().get('token')
    if not token:
        pytest.fail("Token not found in response")
    
    # Получаем список компаний
    companies_response = auth_api.get_companies_list(token)
    if companies_response.status_code != 200:
        pytest.fail(
            f"Failed to get companies list. Status: {companies_response.status_code}. "
            f"Response: {companies_response.text}"
        )
    
    companies = companies_response.json()
    if not companies:
        pytest.skip("No companies available")
    
    company_id = companies[0]['id']
    
    return {
        "token": token,
        "company_id": company_id
    }

@pytest.fixture
def valid_token(valid_token_and_company):
    return valid_token_and_company["token"]

@pytest.fixture
def company_id(valid_token_and_company):
    return valid_token_and_company["company_id"]

@pytest.fixture
def created_project(valid_token, company_id, projects_api):
    response = projects_api.create_project(
        token=valid_token,
        company_id=company_id,
        title="Test Project"
    )
    if response.status_code != 201:
        pytest.fail(f"Failed to create test project. Response: {response.text}")
    
    project_id = response.json()['id']
    yield project_id
    
    # Удаляем проект после теста
    delete_response = projects_api.delete_project(valid_token, project_id)
    if delete_response.status_code not in [200, 204]:
        import logging
        logging.warning(f"Failed to delete test project {project_id}")
