# test_app.py
# Author: Kehinde Omokungbe


import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    """Test the index route"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Your expected content' in response.data  # Update based on actual content

def test_results(client):
    """Test the results route"""
    response = client.get('/results')
    assert response.status_code == 200
    assert b'Your expected content' in response.data  # Update based on actual content

def test_vote_submission(client):
    """Test submitting a vote"""
    # Mock or set up a candidate with ID 1
    response = client.post('/vote/1', data={'field': 'value'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Your expected content after voting' in response.data  # Update based on actual content
