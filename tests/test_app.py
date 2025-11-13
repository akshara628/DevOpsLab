import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_hello(self):
        response = self.client.get('/?name=John&age=20')
        self.assertIn(b'Hello John, you are 20 years old.', response.data)

if __name__ == '__main__':
    unittest.main()
