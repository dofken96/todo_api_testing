import pytest
from data.payloads.payloads_generator import update_task_payload, new_task_payload


@pytest.mark.positive_test
def test_update_task_update(base_url, api_session):

    payload = new_task_payload()
    response_create = api_session.put(f"{base_url}/create-task", json=payload)

    payload_update = update_task_payload(response_create.json()['task']['task_id'])
    response_update = api_session.put(f"{base_url}/update-task", json=payload_update)

    assert response_update.json() == {'updated_task_id': f'{response_create.json()["task"]["task_id"]}'}


    get_response = api_session.get(f"{base_url}/get-task/{response_create.json()['task']['task_id']}")

    assert get_response.json()['content'] == payload_update['content']
    assert get_response.json()['is_done'] == payload_update['is_done']



@pytest.mark.xfail(reason = 'Known issue')
def test_update_task_with_non_existent_task_id(base_url, api_session):

    non_existent_task_id = 999999
    payload_update = update_task_payload(non_existent_task_id)
    response_update = api_session.put(f"{base_url}/update-task", json=payload_update)

    assert response_update.status_code == 422


