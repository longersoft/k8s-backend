import unittest
from unittest.mock import patch
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-secret-key'

# Sample data
books = [
    {'id': 1, 'title': 'Book 1', 'author': 'Author 1'},
    {'id': 2, 'title': 'Book 2', 'author': 'Author 2'},
    {'id': 3, 'title': 'Book 3', 'author': 'Author 3'}
]


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_books(self):
        with app.test_request_context():
            response = self.client.get('/books')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json), 3)

    def test_get_book(self):
        with app.test_request_context():
            response = self.client.get('/books/1')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['id'], 1)

    @patch('app.request')
    def test_add_book(self, mock_request):
        with app.test_request_context():
            mock_request.json.return_value = {
                'id': 4, 'title': 'Book 4', 'author': 'Author 4'}
            response = self.client.post(
                '/books', json={'id': 4, 'title': 'Book 4', 'author': 'Author 4'})
            self.assertEqual(response.status_code, 201)
            self.assertEqual(len(books), 4)


if __name__ == '__main__':
    unittest.main()
