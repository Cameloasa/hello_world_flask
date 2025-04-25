from app import app
from datetime import datetime


def test_hello():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode() == 'Hello, World!'

def test_not_found():
    client = app.test_client()
    response = client.get('/invalid-route')
    assert response.status_code == 404

def test_greet():
    client = app.test_client()
    response = client.get('/greet/Alice')
    assert response.status_code == 200
    assert response.data.decode() == 'Hello, Alice!'

def test_date():
    client = app.test_client()
    response = client.get('/date')
    assert response.status_code == 200
    assert  response.data.decode() == f'Current date: {datetime.now().strftime("%Y-%m-%d")}'

def test_submit():
    client = app.test_client()
    response = client.post('/submit', data={'name': 'Alice'})
    assert response.status_code == 200
    assert response.data.decode() == 'Hello, Alice!'
