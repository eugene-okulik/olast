import requests
import allure
from .main_endpoint import Endpoint


class UpdatePost(Endpoint):
    @allure.step('Изменение объекта методом PUT')
    def update_object_put(self, object_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.base_url}/{object_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response

    @allure.step('Изменение объекта методом PATCH')
    def update_object_patch(self, object_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.base_url}/{object_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
