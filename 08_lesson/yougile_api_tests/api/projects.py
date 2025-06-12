import requests

class ProjectsAPI:
    def __init__(self, base_url="https://ru.yougile.com/api-v2"):
        self.base_url = base_url
    
    def create_project(self, token: str, company_id: str, title: str):
        """Создание проекта"""
        url = f"{self.base_url}/projects"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        payload = {
            "title": title,
            "companyId": company_id
        }
        response = requests.post(url, headers=headers, json=payload)
        return response
     
    def get_project(self, token: str, project_id: str):
        """Получение проекта по ID"""
        url = f"{self.base_url}/projects/{project_id}"
        headers = {
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(url, headers=headers)
        return response
    
    def update_project(self, token: str, project_id: str, title: str):
        """Обновление проекта"""
        url = f"{self.base_url}/projects/{project_id}"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        payload = {
            "title": title
        }
        response = requests.put(url, headers=headers, json=payload)
        return response
    
    def delete_project(self, token: str, project_id: str):
        """Удаление проекта"""
        url = f"{self.base_url}/projects/{project_id}"
        headers = {
            "Authorization": f"Bearer {token}"
        }
        response = requests.delete(url, headers=headers)
        return response
