import pytest
from data.payloads.payloads_generator import new_task_payload



@pytest.mark.positive_test
def test_delete_task(base_url, api_session):

    payload = new_task_payload()
    response_create = api_session.put(f"{base_url}/create-task", json=payload)
    response_delete = api_session.delete(f"{base_url}/delete-task/{response_create.json()['task']['task_id']}")

    assert response_delete.status_code == 200

    response_get_deleted_task = api_session.get(f"{base_url}/get-task/{response_create.json()['task']['task_id']}")
    assert response_get_deleted_task.status_code == 404


@pytest.mark.xfail(reason = 'Known issue')
def test_delete_non_existent_task(base_url, api_session):

    task_ids = [1, 2, 3, 4, 5]
    non_existent_task_id = 999999

    if non_existent_task_id not in task_ids:
        response_delete = api_session.delete(f"{base_url}/delete-task/{non_existent_task_id}")
        assert response_delete.status_code == 404
    else:
        pytest.skip(f"Task with id {non_existent_task_id} exists, cannot perform negative test for deleting non-existent task.")

