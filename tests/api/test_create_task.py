import pytest
from data.payloads.payloads_generator import new_task_payload


@pytest.mark.positive_test
def test_create_task(base_url, api_session):
    payload = new_task_payload()
    response = api_session.put(f"{base_url}/create-task", json=payload)

    assert response.status_code == 200

    body = response.json()
    assert body['task']['content'] == payload['content']
    assert body['task']['user_id'] == payload['user_id']
    assert body['task']['is_done'] == payload['is_done']


@pytest.mark.negative_test
def test_create_task_with_missing_content(base_url, api_session):
    payload = new_task_payload()
    del payload['content']
    response = api_session.put(f"{base_url}/create-task", json=payload)

    assert response.status_code == 422


@pytest.mark.xfail(reason = 'Known issue')
def test_create_task_with_missing_user_id(base_url, api_session):
    payload = new_task_payload()
    del payload['user_id']
    response = api_session.put(f"{base_url}/create-task", json=payload)

    assert response.status_code == 422


@pytest.mark.xfail(reason = 'Known issue')
def test_create_task_with_missing_is_done(base_url, api_session):
    payload = new_task_payload()
    del payload['is_done']
    response = api_session.put(f"{base_url}/create-task", json=payload)

    assert response.status_code == 422


