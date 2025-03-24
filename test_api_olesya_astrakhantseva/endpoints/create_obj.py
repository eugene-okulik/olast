import requests
import allure
from .main_endpoint import Endpoint


class CreatePost(Endpoint):
    @allure.step('Создание нового объекта')
    def create_new_object(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.base_url,
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        self.post_id = self.json['id']
        return self.json
