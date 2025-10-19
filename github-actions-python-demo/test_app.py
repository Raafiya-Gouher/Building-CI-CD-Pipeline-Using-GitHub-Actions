# test_app.py
# ------------------------------
# Simple test to ensure Flask app responds correctly.
# ------------------------------

from app import app

def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Hello from GitHub Actions" in response.data
