import requests
import pytest
import allure

base_url = 'http://167.172.172.115:52353/object'
headers = {'Content-Type': 'application/json'}

# Функция для создания объекта
def create_object():
    body = {
        "name": "qa",
        "data": {
            "capibara": "one"
        }
    }
    response = requests.post(f'{base_url}', json=body, headers=headers)
    post_id = response.json().get('id')
    return post_id


# Функция для удаления объекта
def delete_object(post_id):
    with allure.step(f"Удаление объекта с id {post_id}"):
        get_response = requests.get(f'{base_url}/{post_id}', headers=headers)
        if get_response.status_code == 200:
            delete_response = requests.delete(f'{base_url}/{post_id}', headers=headers)
            assert delete_response.status_code == 200, (
                f'Ошибка при удалении сущности, статус код - {delete_response.status_code}'
            )
            allure.attach(str(post_id), name="ID удалённого объекта", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(str(post_id), name="ID несуществующего объекта", attachment_type=allure.attachment_type.TEXT)


@allure.feature('Objects')
@allure.title('Создание нового объекта')
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite('Создание объекта')
@allure.story('Создание объекта')
def test_create_object():
    # Создание объекта
    post_id = create_object()

    with allure.step("Проверка статус кода 200"):
        get_response = requests.get(f'{base_url}/{post_id}', headers=headers)
        assert get_response.status_code == 200, (
            f'Ошибка при получении сущности, статус код - {get_response.status_code}'
        )

    with allure.step("Проверка содержания данных: id, name и data"):
        obj = get_response.json()
        assert obj['id'] == post_id
        assert obj['name'] == "qa"
        assert obj['data'] == {"capibara": "one"}
        allure.attach(str(obj), name="Тело объекта", attachment_type=allure.attachment_type.JSON)

    # Удаление объекта после теста
    delete_object(post_id)


@allure.feature('Objects')
@allure.title('Изменение объекта методом PUT')
@allure.severity(allure.severity_level.NORMAL)
@allure.suite('Изменение объекта')
@allure.story('Изменение объекта')

def test_change_put():
    # Создание объекта
    post_id = create_object()

    with allure.step("Изменение объекта методом PUT"):
        update_body = {
            "name": "qa_put",
            "data": {"capibara": "two"}
        }
        put_response = requests.put(f'{base_url}/{post_id}', json=update_body, headers=headers)

    with allure.step("Проверка статус кода 200"):
        assert put_response.status_code == 200, (
            f'Ошибка при изменении сущности, статус код - {put_response.status_code}'
        )

    with allure.step("Проверка тела объекта"):
        obj = put_response.json()
        assert obj['name'] == 'qa_put', (
            f'Ожидалось "qa_put", но было получено {obj["name"]}'
        )
        assert obj['data'] == {"capibara": "two"}, (
            f'Ожидалось "{{capibara": "two"}}, но было получено {obj["data"]}'
        )
        allure.attach(str(obj), name="Тело объекта", attachment_type=allure.attachment_type.JSON)

    # Удаление объекта после теста
    delete_object(post_id)


@allure.feature('Objects')
@allure.title('Изменение объекта методом PATCH')
@allure.severity(allure.severity_level.NORMAL)
@allure.suite('Изменение объекта')
@allure.story('Изменение объекта')
def test_change_patch():
    # Создание объекта
    post_id = create_object()

    with allure.step("Изменение объекта методом PATCH"):
        patch_body = {
            "name": "qa_patch",
        }
        patch_response = requests.patch(f'{base_url}/{post_id}', json=patch_body, headers=headers)

    with allure.step("Проверка статус кода 200"):
        assert patch_response.status_code == 200, (
            f'Ошибка при частичном изменении сущности, статус код - {patch_response.status_code}'
        )

    with allure.step("Проверка тела объекта"):
        obj = patch_response.json()
        assert obj['name'] == 'qa_patch', (
            f'Ожидалось "qa_patch", но было получено {obj["name"]}'
        )
        allure.attach(str(obj), name="Тело объекта", attachment_type=allure.attachment_type.JSON)

    # Удаление объекта после теста
    delete_object(post_id)


@allure.feature('Objects')
@allure.title('Удаление объекта')
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite('Удаление объекта')
@allure.story('Удаление объекта')
def test_delete_post():
    # Создание объекта
    post_id = create_object()

    # Удаление объекта
    delete_object(post_id)

    with allure.step("Проверка, что объект был удалён"):
        get_response = requests.get(f'{base_url}/{post_id}', headers=headers)
        assert get_response.status_code == 404, (
            f'Сущность с id {post_id} не была удалена, статус код - {get_response.status_code}'
        )