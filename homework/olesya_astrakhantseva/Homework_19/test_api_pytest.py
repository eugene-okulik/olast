import pytest
import requests

base_url = 'http://167.172.172.115:52353/object'
headers = {'Content-Type': 'application/json'}


# Фикстура для глобальных сообщений
@pytest.fixture(scope='session', autouse=True)
def print_info():
    print('\nStart testing')
    yield
    print('\nTesting completed')


# Фикстура для создания и удаления объекта после теста
@pytest.fixture
def create_post(request):
    def _create_post(name, data):
        body = {
            "name": name,
            "data": data
        }
        response = requests.post(f'{base_url}', json=body, headers=headers)

        assert response.status_code == 200, (
            f'Ошибка при создании сущности, статус код - {response.status_code}'
        )
        assert 'id' in response.json(), 'Тело ответа не содержит поле id'

        post_id = response.json()['id']

        # Создаю финализатор для удаления сущности
        def delete_post():
            delete_response = requests.delete(f'{base_url}/{post_id}')
            assert delete_response.status_code == 200, (
                f'Ошибка при удалении сущности, статус код - {delete_response.status_code}'
            )

            expected_text_body = f'Object with id {post_id} successfully deleted'
            assert delete_response.text == expected_text_body, (f'Ожидалось тело ответа {expected_text_body},'
                                                                f'но было получено {delete_response.text}')

            get_response = requests.get(f'{base_url}/{post_id}', headers=headers)
            assert get_response.status_code == 404, (
                f'Сущность с id {post_id} не была удалена, статус код - {get_response.status_code}'
            )

        request.addfinalizer(delete_post)

        return post_id

    return _create_post


# Фикстура для логирования перед и после теста
@pytest.fixture(autouse=True)
def test_lifecycle():
    print('\nbefore test')
    yield
    print('\nafter test')


# Тест на создание объекта с параметризацией
@pytest.mark.parametrize("name, data", [
    ("qa1", {"cat": "dusa"}),
    ("qa2", {"cat": "vasa"}),
    ("qa3", {"cat": "petya"}),
])
@pytest.mark.critical
def test_create_object(create_post, name, data, print_info):
    post_id = create_post(name, data)

    response = requests.get(f'{base_url}/{post_id}', headers=headers)
    assert response.status_code == 200
    obj = response.json()
    assert obj['id'] == post_id
    assert obj['name'] == name
    assert obj['data'] == data


@pytest.mark.medium
def test_change_put(create_post):
    post_id = create_post("qa_initial", {"cat": "dusa"})
    body = {
        "name": "qa_put",
        "data": {
            "cat": "dusa_2"
        }
    }
    response = requests.put(f'{base_url}/{post_id}', json=body, headers=headers)
    assert response.status_code == 200

    update_name = response.json().get('name')
    update_data = response.json().get('data')

    assert update_name == 'qa_put', (
        f'Ожидалось "qa_put", но было получено {update_name}'
    )
    assert update_data == {"cat": "dusa_2"}, (
        f'Ожидалось "{{cat": "dusa_2"}}, но было получено {update_data}'
    )


def test_change_patch(create_post):
    post_id = create_post("qa_initial", {"cat": "dusa"})
    body = {
        "name": "qa_patch"
    }
    response = requests.patch(f'{base_url}/{post_id}', json=body, headers=headers)
    assert response.status_code == 200

    update_name = response.json().get('name')

    assert update_name == 'qa_patch', (
        f'Ожидалось "qa_patch", но было получено {update_name}'
    )


def test_delete_object(create_post):
    post_id = create_post("qa_delete", {"cat": "delete_me"})

    get_response_before = requests.get(f'{base_url}/{post_id}', headers=headers)
    assert get_response_before.status_code == 200, (
        f'Сущность с id {post_id} не найдена до удаления, статус код - {get_response_before.status_code}'
    )
    # Объект будет удалён автоматически через финализатор
    # Здесь просто проверка что финализатор работает как надо
