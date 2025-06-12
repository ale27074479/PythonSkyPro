import requests
import os
from dotenv import load_dotenv
import logging

load_dotenv()

class AuthAPI:
    def __init__(self, base_url="https://ru.yougile.com/api-v2"):
        self.base_url = base_url
        self.login = os.getenv('YOUGILE_LOGIN')
        self.password = os.getenv('YOUGILE_PASSWORD')
        self.company_id = os.getenv('YOUGILE_COMPANY_ID')
        
        if not self.login or not self.password:
            raise ValueError("YOUGILE_LOGIN and YOUGILE_PASSWORD must be set in .env file")

    def create_auth_key(self):
        """Создание ключа авторизации"""
        url = f"{self.base_url}/auth/login"
        headers = {"Content-Type": "application/json"}
        payload = {"login": self.login, "password": self.password}
        
        if self.company_id:
            payload["companyId"] = self.company_id
            
        response = requests.post(url, json=payload, headers=headers)
        logging.debug(f"Auth response: {response.status_code} - {response.text}")
        return response

    def get_companies_list(self, token):
        """Получение списка компаний"""
        url = f"{self.base_url}/auth/companies"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers)
        return response
