import pytest
import requests




@pytest.fixture
def base_url():
    return 'https://todo.pixegami.io'


@pytest.fixture
def api_session():
    session = requests.Session()
    session.headers.update({'Content-Type': 'application/json'})
    return session


@pytest.fixture
def auth_headers():
    # In a real scenario, you would obtain a token from an auth endpoint
    # For testing purposes, we can use a dummy token or skip auth if not required
    token = 'dummy_token_for_testing'
    return {
        'Authorization': f'Bearer {token}'
    }
