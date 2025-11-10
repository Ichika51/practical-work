import pytest
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_route(client):
    """Тест главной страницы"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, User!" in response.data

def test_hello_content(client):
    """Тест содержимого ответа"""
    response = client.get('/')
    assert response.get_data(as_text=True) == "Hello, User!"

def test_health_route():
    """Тест health check страницы"""
    with app.test_client() as client:
        response = client.get('/health')
        assert response.status_code == 200
        assert b"OK" in response.data