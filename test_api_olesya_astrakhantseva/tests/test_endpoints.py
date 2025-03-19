import pytest
import allure

CREATE_DATA = [
    {"data": {"cat": "dusa"}, "name": "qa1"},
    {"data": {"cat": "vasa"}, "name": "qa2"},
]

PUT_DATA = [
    {"data": {"cat": "dusa_2"}, "name": "qa_put"}
]

PATCH_DATA = [
    {"name": "qa_patch"}
]


@allure.title('Создание нового объекта')
@allure.feature('Objects')
@allure.suite('Создание объекта')
@allure.story('Создание объекта')
@pytest.mark.parametrize('data', CREATE_DATA)
def test_create_object(create_post_endpoint, data):
    create_post_endpoint.create_new_object(payload=data)
    create_post_endpoint.check_status_code_is_200()
    create_post_endpoint.check_response_data(data)


@allure.title('Получение объекта')
@allure.feature('Objects')
@allure.suite('Получение объекта')
@allure.story('Получение объекта')
def test_get_object(get_post_endpoint, post_id):
    get_post_endpoint.get_obj_by_id(post_id)
    get_post_endpoint.check_status_code_is_200()
    get_post_endpoint.check_response_name_is_correct("qa_initial")


@allure.title('Изменение объекта методом PUT')
@allure.feature('Objects')
@allure.suite('Изменение объекта')
@allure.story('Изменение объекта')
@pytest.mark.parametrize('put_data', PUT_DATA)
def test_update_object_put(update_post_endpoint, post_id, put_data):
    update_post_endpoint.update_object_put(post_id, put_data)
    update_post_endpoint.check_status_code_is_200()
    update_post_endpoint.check_response_name_is_correct(put_data["name"])


@allure.title('Изменение объекта методом PATCH')
@allure.feature('Objects')
@allure.suite('Изменение объекта')
@allure.story('Изменение объекта')
@pytest.mark.parametrize('patch_data', PATCH_DATA)
def test_update_object_patch(update_post_endpoint, post_id, patch_data):
    update_post_endpoint.update_object_patch(post_id, patch_data)
    update_post_endpoint.check_status_code_is_200()
    update_post_endpoint.check_response_name_is_correct(patch_data["name"])


@allure.title('Удаление объекта')
@allure.feature('Objects')
@allure.suite('Удаление объекта')
@allure.story('Удаление объекта')
def test_delete_object(delete_post_endpoint, post_id, get_post_endpoint):
    delete_post_endpoint.delete_obj(post_id)
    delete_post_endpoint.check_status_code_is_200()
    delete_post_endpoint.get_body_text_after_delete(post_id)
