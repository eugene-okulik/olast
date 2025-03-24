import pytest
import allure
from endpoints.create_obj import CreatePost
from endpoints.update_obj import UpdatePost
from endpoints.delete_obj import DeleteObj
from endpoints.get_obj import GetPost


@allure.title('Создание нового объекта')
@pytest.fixture()
def create_post_endpoint():
    """Фикстура для создания объекта"""
    return CreatePost()


@pytest.fixture()
def update_post_endpoint():
    """Фикстура для изменения объекта"""
    return UpdatePost()


@pytest.fixture()
def delete_post_endpoint():
    """Фикстура для удаления объекта."""
    return DeleteObj()


@pytest.fixture()
def get_post_endpoint():
    """Фикстура для получения объекта."""
    return GetPost()


@pytest.fixture()
def post_id(create_post_endpoint):
    """Фикстура для создания объекта перед тестом и получения его id"""
    payload = {"name": "qa_initial", "data": {"cat": "dusa"}}
    create_post_endpoint.create_new_object(payload)
    yield create_post_endpoint.post_id
