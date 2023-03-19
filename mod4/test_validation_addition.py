import unittest

from validators_addition import app


class TestValidatorsAddition(unittest.TestCase):
    def setUp(self) -> None:
        app.config["WTF_CSRF_ENABLED"] = False
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def test_email_correct(self):
        data = {
            'email': 'test@test.com',
            'phone': '1111111111',
            'name': 'test',
            'address': 'test',
            'index': '111111'
        }
        response = self.app.post('/registration', json=data)
        self.assertTrue(f'User' in response.text)

    def test_email_incorrect(self):
        data = {
            'email': 'testtest.com',
            'phone': '1111111111',
            'name': 'test',
            'address': 'test',
            'index': '111111'
        }
        response = self.app.post('/registration', json=data)
        self.assertTrue(f'Invalid input:' in response.text)

    def test_no_email(self):
        data = {
            'phone': '1111111111',
            'name': 'test',
            'address': 'test',
            'index': '111111'
        }
        response = self.app.post('/registration', json=data)
        self.assertTrue(f'Invalid input:' in response.text)

    def test_phone_correct(self):
        data = {
            'email': 'test@test.com',
            'phone': '1111111111',
            'name': 'test',
            'address': 'test',
            'index': '111111'
        }
        response = self.app.post('/registration', json=data)
        self.assertTrue(f'User' in response.text)

    def test_phone_incorrect_shorted_number(self):
        data = {
            'email': 'test@test.com',
            'phone': '324',
            'name': 'test',
            'address': 'test',
            'index': '111111'
        }
        response = self.app.post('/registration', json=data)
        self.assertTrue(f'Invalid input:' in response.text)

    def test_phone_incorrect_longer_number(self):
        data = {
            'email': 'test@test.com',
            'phone': '546345242464734536',
            'name': 'test',
            'address': 'test',
            'index': '111111'
        }
        response = self.app.post('/registration', json=data)
        self.assertTrue(f'Invalid input:' in response.text)

    def test_phone_incorrect_not_a_number(self):
        data = {
            'email': 'test@test.com',
            'phone': 'test32842',
            'name': 'test',
            'address': 'test',
            'index': '111111'
        }
        response = self.app.post('/registration', json=data)
        self.assertTrue(f'Invalid input:' in response.text)

    def test_no_phone(self):
        data = {
            'email': 'test@test.com',
            'name': 'test',
            'address': 'test',
            'index': '111111'
        }
        response = self.app.post('/registration', json=data)
        self.assertTrue(f'Invalid input:' in response.text)

    def test_name(self):
        data = {
            'email': 'test@test.com',
            'phone': '1111111111',
            'name': 'test',
            'address': 'test',
            'index': '111111'
        }
        response = self.app.post('/registration', json=data)
        self.assertTrue(f'User' in response.text)

    def test_no_name(self):
        data = {
            'email': 'test@test.com',
            'phone': '1111111111',
            'address': 'test',
            'index': '111111'
        }
        response = self.app.post('/registration', json=data)
        self.assertTrue(f'Invalid input:' in response.text)

    def test_address(self):
        data = {
            'email': 'test@test.com',
            'phone': '1111111111',
            'name': 'test',
            'address': 'test',
            'index': '111111'
        }
        response = self.app.post('/registration', json=data)
        self.assertTrue(f'User' in response.text)

    def test_no_address(self):
        data = {
            'email': 'test@test.com',
            'phone': '1111111111',
            'name': 'test',
            'index': '111111'
        }
        response = self.app.post('/registration', json=data)
        self.assertTrue(f'Invalid input:' in response.text)

    def test_index(self):
        data = {
            'email': 'test@test.com',
            'phone': '1111111111',
            'name': 'test',
            'address': 'test',
            'index': '111111'
        }
        response = self.app.post('/registration', json=data)
        self.assertTrue(f'User' in response.text)

    def test_no_index(self):
        data = {
            'email': 'test@test.com',
            'phone': '1111111111',
            'name': 'test',
            'address': 'test',
        }
        response = self.app.post('/registration', json=data)
        self.assertTrue(f'Invalid input:' in response.text)

    def test_comment(self):
        data = {
            'email': 'test@test.com',
            'phone': '1111111111',
            'name': 'test',
            'address': 'test',
            'index': '111111',
            'comment': 'test'
        }
        response = self.app.post('/registration', json=data)
        self.assertTrue(f'User' in response.text)

    def test_no_comment(self):
        data = {
            'email': 'test@test.com',
            'phone': '1111111111',
            'name': 'test',
            'address': 'test',
            'index': '111111'
        }
        response = self.app.post('/registration', json=data)
        self.assertTrue(f'User' in response.text)
