import unittest

from validators_addition import app

DATA = {
    'email': 'test@test.com',
    'phone': '1111111111',
    'name': 'test',
    'address': 'test',
    'index': '111111'
}


class TestValidatorsAddition(unittest.TestCase):
    def setUp(self) -> None:
        app.config["WTF_CSRF_ENABLED"] = False
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    @classmethod
    def setUpClass(cls):
        global DATA

    def test_email_correct(self):
        response = self.app.post('/registration', json=DATA)
        self.assertTrue(f'User' in response.text)

    def test_email_incorrect(self):
        DATA['email'] = 'testtest.com'
        response = self.app.post('/registration', json=DATA)
        self.assertTrue(f'Invalid input:' in response.text)

    def test_no_email(self):
        del DATA['email']
        response = self.app.post('/registration', json=DATA)
        self.assertTrue(f'Invalid input:' in response.text)

    def test_phone_correct(self):
        DATA['phone'], DATA['name'], DATA['address'], DATA['index'] = '1111111111', 'test', 'test', '111111'
        response = self.app.post('/registration', json=DATA)
        self.assertTrue(f'User' in response.text)

    def test_phone_incorrect_shorted_number(self):
        DATA['phone'] = '324'
        response = self.app.post('/registration', json=DATA)
        self.assertTrue(f'Invalid input:' in response.text)

    def test_phone_incorrect_longer_number(self):
        DATA['phone'] = '2731982654986109'
        response = self.app.post('/registration', json=DATA)
        self.assertTrue(f'Invalid input:' in response.text)

    def test_phone_incorrect_not_a_number(self):
        DATA['phone'] = 'aksjda7a3'
        response = self.app.post('/registration', json=DATA)
        self.assertTrue(f'Invalid input:' in response.text)

    def test_no_phone(self):
        DATA['email'], DATA['name'], DATA['index'] = 'test@test.com', 'test', '111111'
        del DATA['phone']
        response = self.app.post('/registration', json=DATA)
        self.assertTrue(f'Invalid input:' in response.text)

    def test_name(self):
        DATA['email'] = 'test@test.com'
        response = self.app.post('/registration', json=DATA)
        self.assertTrue(f'User' in response.text)

    def test_no_name(self):
        DATA['email'], DATA['index'] = 'test@test.com', '111111'
        del DATA['name']
        response = self.app.post('/registration', json=DATA)
        self.assertTrue(f'Invalid input:' in response.text)

    def test_address(self):
        response = self.app.post('/registration', json=DATA)
        self.assertTrue(f'User' in response.text)

    def test_no_address(self):
        del DATA['address']
        response = self.app.post('/registration', json=DATA)
        self.assertTrue(f'Invalid input:' in response.text)

    def test_index(self):
        DATA['email'] = 'test@test.com'
        response = self.app.post('/registration', json=DATA)
        self.assertTrue(f'User' in response.text)

    def test_no_index(self):
        del DATA['index']
        DATA['email'], DATA['address'] = 'test@test.com', 'test'
        response = self.app.post('/registration', json=DATA)
        self.assertTrue(f'Invalid input:' in response.text)

    def test_comment(self):
        DATA['comment'] = 'test'
        response = self.app.post('/registration', json=DATA)
        self.assertTrue(f'User' in response.text)

    def test_no_comment(self):
        DATA['address'] = 'test'
        del DATA['comment']
        response = self.app.post('/registration', json=DATA)
        self.assertTrue(f'User' in response.text)
