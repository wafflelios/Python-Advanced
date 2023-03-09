import unittest
from flask import Flask
from datetime import datetime

from have_a_good_day import app

WEEKDAYS_TUPLE = ('понедельника', 'вторника', 'среды', 'четверга', 'пятницы', 'субботы', 'воскресенья')


class TestHaveAGoodDay(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test_correct_username(self):
        username = 'test_name'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    def test_correct_weekday(self):
        weekday = WEEKDAYS_TUPLE[datetime.today().weekday()]
        response = self.app.get(self.base_url + 'test_name')
        response_text = response.data.decode()
        self.assertTrue(weekday in response_text)
