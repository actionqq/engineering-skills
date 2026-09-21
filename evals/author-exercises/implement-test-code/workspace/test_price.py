import unittest
from price import total

class PriceTests(unittest.TestCase):
    def test_worked_examples(self):
        for unit_price, quantity, expected in [(125, 3, 375), (125, 0, 0), (0, 9, 0), (7, 1, 7)]:
            with self.subTest(unit_price=unit_price, quantity=quantity):
                self.assertEqual(total(unit_price, quantity), expected)
