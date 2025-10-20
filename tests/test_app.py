# test_app.py
# ------------------------------
# Simple test to ensure Flask app responds correctly.
# ------------------------------

import pytest
from app import app

# Fixture to create a test client
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test the homepage
def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data
