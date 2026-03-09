import pytest
from data.payloads.payloads_generator import new_task_payload

@pytest.mark.positive_test
def test_get_list_tasks(base_url, api_session):

    """new created tasks"""
    new_created_tasks = []

    for _ in range(3):
        payload = new_task_payload()
        response_create = api_session.put(f"{base_url}/create-task", json=payload)
        new_created_tasks.append(response_create.json()['task'])

    """extracted the created tasks from response"""
    extracted_tasks_from_response = []

    for i in range(3):
        response_get_list_tasks = api_session.get(f"{base_url}/list-tasks/{new_created_tasks[i-1]['user_id']}")
        assert response_get_list_tasks.status_code == 200
        extracted_tasks_from_response.append(response_get_list_tasks.json()['tasks'])

    assert len(extracted_tasks_from_response) == 3




@pytest.mark.xfail(reason = 'Known issue')
def test_get_list_tasks_negative(base_url, api_session):

    existed_user_id = [1, 2, 3, 4, 5]

    unexisted_user_id = 123124124

    if unexisted_user_id not in existed_user_id:
        response_get = api_session.get(f"{base_url}/list-tasks/{unexisted_user_id}")
        assert response_get.status_code == 404
