import unittest

from armstrong_numbers import (
    is_armstrong_number,
)

class ArmstrongNumbersTest(unittest.TestCase):
    def test_zero_is_armstrong_number(self):
        self.assertIs(is_armstrong_number(0), True)