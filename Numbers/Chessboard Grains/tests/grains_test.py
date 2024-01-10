import unittest

from grains import (
    square,
    total,
)

class GrainsTest(unittest.TestCase):
    def test_grains_on_square_1(self):
        self.assertEqual(square(1), 1)

    def test_grains_on_square_2(self):
        self.assertEqual(square(2), 2)
    
    def test_grains_on_square_3(self):
        self.assertEqual(square(3), 4)