import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200


def test_get_books(client):
    response = client.get('/books')
    assert response.status_code == 200


def test_get_book(client):
    response = client.get('/books/1')
    assert response.status_code == 200


def test_get_nonexistent_book(client):
    response = client.get('/books/100')
    assert response.status_code == 404


def test_add_book(client):
    data = {
        'id': 4,
        'title': 'New Book',
        'author': 'New Author'
    }
    response = client.post('/books', json=data)
    assert response.status_code == 201


def test_get_nonexistent_route(client):
    response = client.get('/nonexistent_route')
    assert response.status_code == 404
