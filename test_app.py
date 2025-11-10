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
    assert b"Hello, CI/CD World!" in response.data

def test_hello_content(client):
    """Тест содержимого ответа"""
    response = client.get('/')
    assert response.get_data(as_text=True) == "Hello, CI/CD World!"

def test_health_route(client):
    """Тест health check страницы"""
    response = client.get('/health')
    assert response.status_code == 200
    assert b"OK" in response.data

def test_version_route(client):
    """Тест version endpoint"""
    response = client.get('/version')
    assert response.status_code == 200
    assert b"1.0.0" in response.data