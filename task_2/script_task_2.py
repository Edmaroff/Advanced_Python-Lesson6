import requests
import os
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('token')


class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    # Проверка, существует ли папка "Тест" на диске
    def check_folder(self, folder_name='Тест'):
        upload_url = 'https://cloud-api.yandex.net:443/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': folder_name}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.status_code

    # Создание папки "Тест"
    def create_folder(self, folder_name='Тест'):
        upload_url = 'https://cloud-api.yandex.net:443/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': folder_name}
        response = requests.put(upload_url, headers=headers, params=params)
        return response.status_code
