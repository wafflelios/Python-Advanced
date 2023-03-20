import unittest

from exception_stub import BlockErrors


class TestExceptionStub(unittest.TestCase):
    def test_error_is_ignored(self):
        err_types = {ZeroDivisionError, TypeError}
        self.assertTrue(BlockErrors(err_types).__exit__(ZeroDivisionError, 1, 1))

    def test_error_goes_up(self):
        err_types = {ZeroDivisionError}
        self.assertFalse(BlockErrors(err_types).__exit__(TypeError, 1, 1))

    def test_error_is_thrown_higher_in_the_inner_block(self):
        outer_err_types = {TypeError}
        inner_err_types = {ZeroDivisionError}
        self.assertFalse(BlockErrors(inner_err_types).__exit__(TypeError, 1, 1))
        self.assertTrue(BlockErrors(outer_err_types).__exit__(TypeError, 1, 1))

    def test_child_errors_ignored(self):
        err_types = {Exception}
        self.assertTrue(BlockErrors(err_types).__exit__(TypeError, 1, 1))

