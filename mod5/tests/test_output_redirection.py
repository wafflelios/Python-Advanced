import unittest

from output_redirection import Redirect


class TestOutputRedirection(unittest.TestCase):
    def test_two_arguments(self):
        stderr_file = open('stderr.txt', 'w')
        stdout_file = open('stdout.txt', 'w')
        with Redirect(stderr=stderr_file, stdout=stdout_file):
            print('Hello stdout.txt')
            raise Exception('Hello stderr.txt')
        with open('stderr.txt', 'r') as stderr_file:
            self.assertTrue('Hello stderr.txt' in stderr_file.read())
        with open('stdout.txt', 'r') as stdout_file:
            self.assertTrue('Hello stdout.txt' in stdout_file.read())

    def test_out_only(self):
        stdout_file = open('stdout.txt', 'w')
        with Redirect(stdout=stdout_file):
            print('Hello stdout.txt')
        with open('stdout.txt', 'r') as stdout_file:
            self.assertTrue('Hello stdout.txt' in stdout_file.read())

