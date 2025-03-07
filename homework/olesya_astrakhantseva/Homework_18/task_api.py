import requests

base_url = 'http://167.172.172.115:52353/object'
headers = {'Content-Type': 'application/json'}


def create_post():
    body = {
        "name": "qa",
        "data": {
            "capibara": "one"
        }
    }
    response = requests.post(f'{base_url}', json=body, headers=headers)

    assert response.status_code == 200, (
        f'Ошибка при создании сущности, статус код - {response.status_code}'
    )
    assert 'id' in response.json(), 'Тело ответа не содержит поле id'

    return response.json().get('id')


def get_obj_id(post_id):
    response = requests.get(f'{base_url}/{post_id}', headers=headers)
    assert response.status_code == 200, (
        f'Ошибка при загрузке сущности, статус код - {response.status_code}'
    )
    obj = response.json()
    return obj


def change_put(post_id):
    body = {
        "name": "qa_put",
        "data": {
            "capibara": "two"
        }
    }
    response = requests.put(f'{base_url}/{post_id}',
                            json=body, headers=headers)
    assert response.status_code == 200

    update_name = response.json().get('name')
    update_data = response.json().get('data')

    assert update_name == 'qa_put', (
        f'Ожидалось "qa_put", но было получено {update_name}'
    )
    assert update_data == {"capibara": "two"}, (
        f'Ожидалось "{{capibara": "two"}}, но было получено {update_data}'
    )


def change_patch(post_id):
    body = {
        "name": "qa_patch",
    }
    response = requests.patch(f'{base_url}/{post_id}', json=body, headers=headers)
    assert response.status_code == 200

    update_name = response.json().get('name')
    assert update_name == 'qa_patch', (
        f'Ожидалось "qa_patch", но было получено {update_name}'
    )


def delete_post(post_id):
    response = requests.delete(f'{base_url}/{post_id}', headers=headers)
    assert response.status_code == 200, (
        f'Ошибка при удалении сущности, статус код - {response.status_code}'
    )


def deleted_object(post_id):
    response = requests.get(f'{base_url}/{post_id}', headers=headers)
    assert response.status_code == 404, (
        f'Сущность с id {post_id} должна быть удалена, '
        f'но получен статус код {response.status_code}'
    )


def main():
    post_id = create_post()
    print(f'Создана сущность с id: {post_id}')

    init_obj = get_obj_id(post_id)
    print(f'Тело сущности при создании: {init_obj}\n{"=" * 40}')

    change_put(post_id)
    updated_obj_put = get_obj_id(post_id)
    print(f'Изменена сущность методом PUT с id: {post_id}')
    print(f'Тело сущности: {updated_obj_put}\n{"=" * 40}')

    change_patch(post_id)
    updated_obj_patch = get_obj_id(post_id)
    print(f'Изменена сущность методом PATCH с id: {post_id}')
    print(f'Тело сущности после изменения: {updated_obj_patch}\n{"=" * 40}')

    delete_post(post_id)
    print(f'Удалена сущность с id: {post_id}')

    deleted_object(post_id)
    print('Проверка удаленной сущности: успешно')


if __name__ == "__main__":
    main()
