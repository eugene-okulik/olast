import pytest
import requests

from test_api_pytest import base_url
from test_api_pytest import headers


# Фикстура для глобальных сообщений
@pytest.fixture(scope='session', autouse=True)
def print_info():
    print('\nStart testing')
    yield
    print('\nTesting completed')


# Фикстура для создания и удаления объекта через yield
@pytest.fixture
def create_post(request):
    name = request.param.get("name")
    data = request.param.get("data")

    body = {"name": name, "data": data}
    response = requests.post(f'{base_url}', json=body, headers=headers)

    post_id = response.json()['id']

    created_object = {"id": post_id, "name": name, "data": data}
    yield created_object

    requests.delete(f'{base_url}/{post_id}')


# Фикстура для логирования перед и после теста
@pytest.fixture(autouse=True)
def test_lifecycle():
    print('\nbefore test')
    yield
    print('\nafter test')
