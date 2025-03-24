import requests
import allure
from .main_endpoint import Endpoint


class GetPost(Endpoint):
    @allure.step('Получение объекта по ID')
    def get_obj_by_id(self, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            f'{self.base_url}/{object_id}',
            headers=headers
        )
        self.json = self.response.json()
        return self.json
