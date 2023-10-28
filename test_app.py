import app
import pytest
from unittest.mock import patch

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    client = app.app.test_client()
    yield client

@patch('app.app')
def test_hello(mock_app, client):
    mock_app.route.return_value('Hello He4rt Developers 🚀')

    response = client.get('/hello')
    assert response.status_code == 200
    assert "Hello He4rt Developers 🚀" in response.data.decode('utf-8')
