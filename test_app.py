"""Unit tests for Flask application."""
import pytest
from main import app


@pytest.fixture
def client():
    """Create test client."""
    with app.test_client() as test_client:
        yield test_client


def test_hello_endpoint(client):
    """Test hello endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, CI/CD World!" in response.data


def test_health_endpoint(client):
    """Test health endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert b"OK" in response.data


def test_version_endpoint(client):
    """Test version endpoint."""
    response = client.get("/version")
    assert response.status_code == 200
    assert b"1.0.0" in response.data


def test_main_endpoint(client):
    """Test main endpoint integration."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, CI/CD World!" in response.data
