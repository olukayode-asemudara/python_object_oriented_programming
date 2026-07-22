import unittest
from stockApp.stock import Stock
j

class MyTestCase(unittest.TestCase):
    def test_something(self):
        Stock("GTCO", "Guaranteed Co.", 100.0, 78)

    def test_get_symbol(self):
        stock_one = Stock("GTCO", "Guaranteed Co.", 100.0, 78)
        self.assertEqual(stock_one.get_symbol(), "GTCO")

    def test_get_name(self):
        stock_one = Stock("GTCO", "Guaranteed Co.", 100.0, 78)
        self.assertEqual(stock_one.get_name(), "Guaranteed Co.")

    def test_get_previous_closing_price(self):
        stock_one = Stock("GTCO", "Guaranteed Co.", 100.0, 78)
        self.assertEqual(stock_one.get_previous_closing_price(), 100.0)

    def test_valid_symbol_raises_value_error(self):
        stock_one = Stock("GtcO", "Guaranteed Co.", 100.0, 78)
        self.assertEqual(stock_one.get_symbol(), "GTCO")

    def test_set_previous_closing_price(self):
        stock_one = Stock("GTCO", "Guaranteed Co.", 100.0, 78)
        stock_one.set_previous_closing_price(350.0)
        self.assertEqual(stock_one.get_previous_closing_price(), 350.0)

    def test_get_current_price(self):
        stock_one = Stock("GTCO", "Guaranteed Co.", 100.0, 78)
        self.assertEqual(stock_one.get_current_price(), 78.0)

    def test_set_current_price(self):
        stock_one = Stock("GTCO", "Guaranteed Co.", 100.0, 78)
        stock_one.set_current_price(200.0)
        self.assertEqual(stock_one.get_current_price(), 200.0)