import pytest
from app import app, get_all_candidates, get_candidate, vote_for_candidate

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    """Test the index route to ensure candidates are displayed."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Neal Dunn (REP)' in response.data
    assert b'Al Lawson (DEM)' in response.data

def test_vote(client):
    """Test voting functionality."""
    response = client.post('/vote/1', follow_redirects=True)
    assert response.status_code == 200
    assert b'Results' in response.data
    # Additional checks could include ensuring votes are updated in the database.

def test_results(client):
    """Test results route to ensure votes are displayed."""
    response = client.get('/results')
    assert response.status_code == 200
    assert b'Congress Election Results' in response.data
    assert b'Neal Dunn (REP)' in response.data
    assert b'Al Lawson (DEM)' in response.data
