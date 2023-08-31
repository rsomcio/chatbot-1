# tests/test_app.py
import pytest
from unittest.mock import patch
from app import app, get_context, create_chat_completion

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('app.get_db')
def test_get_context(mock_get_db):
    mock_cursor = mock_get_db.return_value.cursor.return_value
    mock_cursor.execute.return_value.fetchone.return_value = ("keyword", "context")
    context = get_context("sample sentence")
    assert context == ("keyword", "context")

@patch('app.requests.request')
def test_create_chat_completion(mock_request):
    mock_response = {
        'choices': [{'message': {'content': 'Generated answer'}}]
    }
    mock_request.return_value.json.return_value = mock_response
    answer = create_chat_completion(("keyword", "context"), "question")
    assert answer == "Generated answer"

def test_hello_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'chatbot 1.0!' in response.data

def test_chat_route(client):
    response = client.post('/chat', json={'prompt': 'question'})
    assert response.status_code == 200
    # Add more assertions based on the expected behavior of your chat route
