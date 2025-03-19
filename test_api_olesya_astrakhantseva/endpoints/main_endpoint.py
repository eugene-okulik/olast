import allure


class Endpoint:
    base_url = "http://167.172.172.115:52353/object"
    headers = {'Content-Type': 'application/json'}
    response = None
    json = None
    post_id = None

    @allure.step('Проверка поля name')
    def check_response_name_is_correct(self, name):
        assert self.json['name'] == name, f"Ожидалось значение {name}, но получено {self.json['name']}"

    @allure.step('Проверка, что статус код равен 200')
    def check_status_code_is_200(self):
        assert self.response.status_code == 200, f"Ожидался статус код 200, но получен {self.response.status_code}"

    @allure.step('Проверка, что статус код равен 404')
    def check_status_code_is_404(self):
        assert self.response.status_code == 404, f"Ожидался статус код 404, но получен {self.response.status_code}"

    @allure.step('Проверка, что данные в ответе соответствуют ожидаемым')
    def check_response_data(self, expected_data):
        actual_data = self.response.json()
        assert actual_data['data'] == expected_data['data'], (
            f"Ожидалось значение {expected_data['data']}, но было получено {actual_data['data']}"
        )
        assert actual_data['name'] == expected_data['name'], (
            f"Ожидалось значение {expected_data['name']}, но было получено {actual_data['name']}"
        )
