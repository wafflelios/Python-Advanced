import unittest

from trust_but_check import Person

sasha = Person('Sasha', 2000, 'home')
alya = Person('Alya', 2003)


class TestTrustButCheck(unittest.TestCase):
    def test_get_age(self):
        self.assertTrue(str(23) in str(sasha.get_age()))

    def test_get_name(self):
        self.assertTrue('Sasha' in sasha.get_name())

    def test_set_name(self):
        sasha.set_name('Alexander')
        self.assertTrue('Alexander' in sasha.get_name())

    def test_set_address(self):
        sasha.set_address('Mira 32')
        self.assertTrue('Mira 32' in sasha.get_address())

    def test_get_address(self):
        self.assertTrue('home' in sasha.get_address())

    def test_is_homeless(self):
        self.assertTrue('True' in str(alya.is_homeless()))
        self.assertTrue('False' in str(sasha.is_homeless()))
