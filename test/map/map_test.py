import unittest
from map.map import Map


class TestMap(unittest.TestCase):

    def setUp(self):
        self.map = Map()

    def test_map_is_empty(self):
        self.assertTrue(self.map.is_empty())

    def test_can_get_size_of_map(self):
        self.assertEqual(0, self.map.size())

    def test_can_put_elements_inside_map(self):
        self.map.put("apple", "a sweet fruit")

        self.assertFalse(self.map.is_empty())
        self.assertEqual(1, self.map.size())

    def test_can_check_whether_map_contains_key(self):
        self.map.put("apple", "fruit")

        self.assertTrue(self.map.contains("apple"))


if __name__ == "__main__":
    unittest.main()