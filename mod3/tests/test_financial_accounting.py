import unittest

from financial_accounting import app

STORAGE = {
    2022: {
        11:
            {5: 1000,
             10: 500}},
    2023: {
        3: {18: 500}
    }}


class TestFinancialAccounting(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    @classmethod
    def setUpClass(cls):
        global STORAGE
        cls.cost = 1000

    def test_add_basic(self):
        """
        выводит информацию о совершенной в рублях трате за какой-то день,
        даже если этого дня и/или месяца не было в STORAGE
        """
        date = '20230310'
        response = self.app.get(f'/add/{date}/{self.cost}')
        response_text = response.data.decode()
        self.assertTrue(str(self.cost) in response_text)

    def test_add_summ(self):
        """
        выводит сумму сувершенных в рублях тратах за какой-то день,
        если их несколько
        """
        date = '20230318'
        year, month, day = int(date[:4]), int(date[4:6]), int(date[6:9])
        response = self.app.get(f'/add/{date}/{self.cost}')
        response_text = response.data.decode()
        self.assertTrue(str(STORAGE[year][month][day] + self.cost) in response_text)

    def test_add_correct_data(self):
        """
        endpoint/add/ может принять дату только в формате YYYYMMDD
        """
        date = '20230231'
        with self.assertRaises(ValueError):
            self.app.get(f'/add/{date}/{self.cost}')

    def test_calculate_year_one_date(self):
        """
        выводит суммарные траты за указанный год (в году одна дата с тратами)
        """
        year = 2023
        response = self.app.get(f'/calculate/{year}')
        response_text = response.data.decode()
        res = str(STORAGE[year][3][18] + 2 * self.cost)
        self.assertTrue(res in response_text)

    def test_calculate_year_few_dates(self):
        """
        выводит суммарные траты за указанный год (в году несколько дат с тратами)
        """
        year = 2022
        response = self.app.get(f'/calculate/{year}')
        response_text = response.data.decode()
        res = str(STORAGE[year][11][5] + STORAGE[2022][11][10])
        self.assertTrue(res in response_text)

    def test_calculate_no_year(self):
        """
        суммарные траты за указанный год равны 0, если этого года нет в STORAGE
        """
        year = 1998
        response = self.app.get(f'/calculate/{year}')
        response_text = response.data.decode()
        self.assertTrue('0' in response_text)

    def test_calculate_year_month_one_date(self):
        """
        выводит суммарные траты за указанный месяц(в месяца одна дата)
        """
        year = 2023
        month = 3
        response = self.app.get(f'/calculate/{year}/{month}')
        response_text = response.data.decode()
        self.assertTrue(str(STORAGE[year][month][18] + 2 * self.cost) in response_text)

    def test_calculate_year_month_few_dates(self):
        """
        выводит суммарные траты за указанный месяц(в месяца несколько дат)
        """
        year = 2022
        month = 11
        response = self.app.get(f'/calculate/{year}/{month}')
        response_text = response.data.decode()
        res = str(STORAGE[year][month][5] + STORAGE[year][month][10])
        self.assertTrue(res in response_text)

    def test_calculate_year_no_month(self):
        """
        суммарные траты за указанный месяц равны 0, если такого месяца нет в STORAGE
        """
        year = 1998
        month = 1
        response = self.app.get(f'/calculate/{year}/{month}')
        response_text = response.data.decode()
        self.assertTrue('0' in response_text)