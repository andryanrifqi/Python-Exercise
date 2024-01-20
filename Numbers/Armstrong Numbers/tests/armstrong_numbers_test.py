import unittest

from armstrong_numbers import (
    is_armstrong_number,
)

class ArmstrongNumbersTest(unittest.TestCase):
    def test_zero_is_armstrong_number(self):
        self.assertIs(is_armstrong_number(0), True)

    def test_single_digit_numbers(self):
        self.assertIs(is_armstrong_number(9), True)

    def test_two_digit_numbers(self):
        self.assertIs(is_armstrong_number(11), False)

    def test_three_digit_numbers_correct(self):
        self.assertIs(is_armstrong_number(153), True)
    
    def test_three_digit_numbers_incorrect(self):
        self.assertIs(is_armstrong_number(154), False)
    
    def test_four_digit_numbers_correct(self):
        self.assertIs(is_armstrong_number(9474), True)
    
    def test_four_digit_numbers_incorrect(self):
        self.assertIs(is_armstrong_number(9475), False)

    def test_seven_digit_numbers_correct(self):
        self.assertIs(is_armstrong_number(9926315), True)
    
    def test_seven_digit_numbers_incorrect(self):
        self.assertIs(is_armstrong_number(9926314), False)