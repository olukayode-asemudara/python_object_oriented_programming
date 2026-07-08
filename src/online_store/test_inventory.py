import unittest

from online_store.inventory import Inventory
from online_store.item import Item


class InventoryTestScenarios(unittest.TestCase):

    def test_add_item_to_inventory(self):
        inventory = Inventory()
        apple = Item("Apple", 1.50, 10)
        inventory.add_item(apple)
        stored_item = inventory.get_item("Apple")
        self.assertIsNotNone(stored_item)
        self.assertEqual("Apple", stored_item.name)
        self.assertEqual(10, stored_item.quantity)


    def test_get_item_that_does_not_exist_returns_none(self):
        inventory = Inventory()
        item = inventory.get_item("Banana")
        self.assertIsNone(item)


    def test_check_item_availability_when_stock_exists(self):
        inventory = Inventory()
        apple_stock = Item("Apple", 1.50, 10)
        inventory.add_item(apple_stock)
        requested_item = Item("Apple", 1.50, 3)
        is_available = inventory.check_availability(requested_item)
        self.assertTrue(is_available)


    def test_check_item_availability_when_stock_is_insufficient(self):
        inventory = Inventory()
        apple_stock = Item("Apple", 1.50, 2)
        inventory.add_item(apple_stock)
        requested_item = Item("Apple", 1.50, 5)
        is_available = inventory.check_availability(requested_item)
        self.assertFalse(is_available)


    def test_remove_stock_reduces_quantity(self):
        inventory = Inventory()
        apple_stock = Item("Apple", 1.50, 10)
        inventory.add_item(apple_stock)
        purchased_item = Item("Apple", 1.50, 4)
        inventory.remove_stock(purchased_item)
        remaining_item = inventory.get_item("Apple")
        self.assertEqual(6, remaining_item.quantity)


    def test_remove_stock_raises_error_when_not_enough_stock(self):
        inventory = Inventory()
        apple_stock = Item("Apple", 1.50, 2)
        inventory.add_item(apple_stock)
        purchased_item = Item("Apple", 1.50, 5)
        with self.assertRaises(ValueError):
            inventory.remove_stock(purchased_item)