# test_app.py
# Author: Kehinde Omokungbe

import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    """Test the index route"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'candidates' in response.data  # Assuming 'candidates' is part of the HTML content

def test_vote(client):
    """Test the vote route with valid candidate ID"""
     # Mock or set up a candidate with ID 1
    response = client.get('/vote/1')
    assert response.status_code == 200
    assert b'Vote' in response.data  # Assuming 'Vote' is part of the HTML content

def test_results(client):
    """Test the results route"""
    response = client.get('/results')
    assert response.status_code == 200
    assert b'results' in response.data  # Assuming 'results' is part of the HTML content

def test_vote_submission(client):
    """Test submitting a vote"""
    # Mock or set up a candidate with ID 1
    response = client.post('/vote/1', data={'field': 'value'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'results' in response.data  # Assuming it redirects to results page

