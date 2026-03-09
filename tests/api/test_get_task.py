import pytest
from data.payloads.payloads_generator import new_task_payload



@pytest.mark.positive_test
def test_get_task(base_url, api_session):

    new_created_tasks = []

    for _ in range(3):
        payload = new_task_payload()
        response_create = api_session.put(f"{base_url}/create-task", json=payload)
        new_created_tasks.append(response_create.json()['task'])


    for i in new_created_tasks:
        response_get_list_tasks = api_session.get(f"{base_url}/get-task/{i['task_id']}")
        assert response_get_list_tasks.status_code == 200
        assert response_get_list_tasks.json()['content'] == i['content']
        assert response_get_list_tasks.json()['user_id'] == i['user_id']
        assert response_get_list_tasks.json()['is_done'] == i['is_done']



@pytest.mark.negative_test
def test_get_non_existent_task(base_url, api_session):

    task_ids = [1, 2, 3, 4, 5]
    non_existent_task_id = 999999

    if non_existent_task_id not in task_ids:
        response_get = api_session.get(f"{base_url}/get-task/{non_existent_task_id}")
        assert response_get.status_code == 404
    else:
        pytest.skip(f"Task with id {non_existent_task_id} exists, cannot perform negative test for getting non-existent task.")
