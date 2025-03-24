import requests
import allure
from .main_endpoint import Endpoint


class DeleteObj(Endpoint):
    @allure.step('Удаление объекта')
    def delete_obj(self, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            f'{self.base_url}/{object_id}',
            headers=headers
        )
        self.text = self.response.text
        return self.response

    @allure.step('Проверка тела ответа при удалении')
    def get_body_text_after_delete(self, post_id):
        expected_text_body = f'Object with id {post_id} successfully deleted'
        assert self.text == expected_text_body, (
            f'Ожидалось тело ответа "{expected_text_body}", но было получено "{self.text}"'
        )
        allure.attach(str(self.text), name="Тело объекта", attachment_type=allure.attachment_type.TEXT)
