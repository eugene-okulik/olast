import pytest
import requests
import allure

base_url = 'http://167.172.172.115:52353/object'
headers = {'Content-Type': 'application/json'}


@allure.title('Создание нового объекта')
@pytest.mark.critical
# Тест на создание объекта с параметризацией
@pytest.mark.parametrize("create_post", [
    {"name": "qa1", "data": {"cat": "dusa"}},
    {"name": "qa2", "data": {"cat": "vasa"}},
    {"name": "qa3", "data": {"cat": "petya"}},
], indirect=True, ids=["qa1", "qa2", "qa3"])

def test_create_object(create_post):
    post_id = create_post["id"]
    name = create_post["name"]
    data = create_post["data"]

    with allure.step('Создание нового объекта'):
        response = requests.get(f'{base_url}/{post_id}', headers=headers)

    with allure.step('Проверка статус кода 200'):
        assert response.status_code == 200, (
            f'Ошибка при получении сущности, статус код - {response.status_code}'
        )

    with allure.step('Проверка содержания данных: id, name и data'):
        obj = response.json()
        assert obj['id'] == post_id
        assert obj['name'] == name
        assert obj['data'] == data
        allure.attach(str(obj), name="Тело объекта", attachment_type=allure.attachment_type.JSON)
        allure.dynamic.feature('Objects')
        allure.dynamic.story('Создание объекта')
        allure.dynamic.severity(allure.severity_level.CRITICAL)
        allure.dynamic.suite('Создание объекта')


@allure.feature('Objects')
@allure.title('Изменение объекта методом PUT')
@allure.severity(allure.severity_level.NORMAL)
@allure.suite('Изменение объекта')
@allure.story('Изменение объекта')
@pytest.mark.medium
@pytest.mark.parametrize("create_post", [
    {"name": "qa_initial", "data": {"cat": "dusa"}}
], indirect=True)
@pytest.mark.medium
def test_change_put(create_post):
    post_id = create_post["id"]

    body = {
        "name": "qa_put",
        "data": {"cat": "dusa_2"}
    }
    with allure.step('Изменение объекта методом PUT'):
        response = requests.put(f'{base_url}/{post_id}', json=body, headers=headers)

    with allure.step('Проверка статус кода 200'):
        assert response.status_code == 200, (
            f'Ошибка при получении сущности, статус код - {response.status_code}'
        )

    with allure.step('Проверка содержания данных: id, name и data'):
        update_name = response.json().get('name')
        update_data = response.json().get('data')

        assert update_name == 'qa_put', (
            f'Ожидалось "qa_put", но было получено {update_name}'
        )
        assert update_data == {"cat": "dusa_2"}, (
            f'Ожидалось "{{cat": "dusa_2"}}, но было получено {update_data}'
        )
        obj = response.json()
        allure.attach(str(obj), name="Тело объекта", attachment_type=allure.attachment_type.JSON)
        allure.dynamic.feature('Objects')
        allure.dynamic.story('Изменение объекта')
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.suite('Изменение объекта')


@allure.feature('Objects')
@allure.title('Изменение объекта методом PATCH')
@allure.severity(allure.severity_level.NORMAL)
@allure.suite('Изменение объекта')
@allure.story('Изменение объекта')
@pytest.mark.medium
@pytest.mark.parametrize("create_post", [
    {"name": "qa_initial", "data": {"cat": "dusa"}}
], indirect=True)
def test_change_patch(create_post):
    post_id = create_post["id"]

    body = {"name": "qa_patch"}

    with allure.step('Изменение объекта методом PATH'):
        response = requests.patch(f'{base_url}/{post_id}', json=body, headers=headers)

    with allure.step('Проверка статус кода 200'):
        assert response.status_code == 200, (
            f'Ошибка при получении сущности, статус код - {response.status_code}'
        )

    with allure.step('Проверка изменения данных name'):
        update_name = response.json().get('name')
        assert update_name == 'qa_patch', (
            f'Ожидалось "qa_patch", но было получено {update_name}'
        )
        obj = response.json()
        allure.attach(str(obj), name="Тело объекта", attachment_type=allure.attachment_type.JSON)
        allure.dynamic.feature('Objects')
        allure.dynamic.story('Изменение объекта')
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.suite('Изменение объекта')


@allure.feature('Objects')
@allure.title('Удаление объекта')
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite('Удаление объекта')
@allure.story('Удаление объекта')
@pytest.mark.critical
@pytest.mark.parametrize("create_post", [
    {"name": "qa_delete", "data": {"cat": "delete_me"}}
], indirect=True)
def test_delete_object(create_post):
    post_id = create_post["id"]

    with allure.step('Удаление объекта'):
        delete_response = requests.delete(f'{base_url}/{post_id}')

    with allure.step('Проверка статус кода 200'):
        assert delete_response.status_code == 200, (
            f'Ошибка при удалении сущности, статус код - {delete_response.status_code}'
        )
        expected_text_body = f'Object with id {post_id} successfully deleted'
        assert delete_response.text == expected_text_body, (
            f'Ожидалось тело ответа "{expected_text_body}", но было получено "{delete_response.text}"'
        )

        get_response = requests.get(f'{base_url}/{post_id}', headers=headers)
        assert get_response.status_code == 404, (
            f'Сущность с id {post_id} не была удалена, статус код - {get_response.status_code}'
        )

        allure.attach(str(delete_response), name="Тело объекта", attachment_type=allure.attachment_type.JSON)
        allure.dynamic.feature('Objects')
        allure.dynamic.story('Удаление объекта')
        allure.dynamic.severity(allure.severity_level.CRITICAL)
        allure.dynamic.suite('Удаление объекта')
