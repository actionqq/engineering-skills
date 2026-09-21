import unittest
from cart import add_item

class CartTests(unittest.TestCase):
    def test_independent_users(self):
        first = add_item("apple")
        second = add_item("pear")
        self.assertEqual(first, ["apple"])
        self.assertEqual(second, ["pear"])
        self.assertIsNot(first, second)

    def test_explicit_cart_is_preserved(self):
        cart = ["existing"]
        self.assertIs(add_item("new", cart), cart)
        self.assertEqual(cart, ["existing", "new"])

    def test_explicit_empty_cart_is_preserved(self):
        cart = []
        self.assertIs(add_item("new", cart), cart)
        self.assertEqual(cart, ["new"])
