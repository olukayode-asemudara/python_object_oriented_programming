import unittest

from online_store.cart import Cart
from online_store.item import Item
from online_store.inventory import Inventory


class StoreTestScenarios(unittest.TestCase):

    def test_checkout_updates_inventory(self):
        inventory = Inventory()
        apple_stock = Item("Apple", 1.50, 10)
        inventory.add_item(apple_stock)
        cart = Cart([], "cart-001")
        apple_purchase = Item("Apple", 1.50, 3)
        cart.add_item(apple_purchase)
        receipt = cart.checkout(inventory)
        self.assertEqual(4.50, receipt["total"])
        remaining_stock = inventory.get_item("Apple")
        self.assertEqual(7, remaining_stock.quantity)


    def test_checkout_fails_when_stock_is_insufficient(self):
        inventory = Inventory()
        apple_stock = Item("Apple", 1.50, 2)
        inventory.add_item(apple_stock)
        cart = Cart([], "cart-002")
        apple_purchase = Item("Apple", 1.50, 5)
        cart.add_item(apple_purchase)
        with self.assertRaises(ValueError):
            cart.checkout(inventory)