import unittest
from src.arrayList.array_list import ArrayList


class TestArrayList(unittest.TestCase):

    def setUp(self):
        self.array_list = ArrayList()

    def test_new_array_list_is_empty(self):
        self.assertTrue(self.array_list.is_empty())

    def test_can_add_element_to_array_list(self):
        self.array_list.add(5)
        self.assertFalse(self.array_list.is_empty())

    def test_can_set_element_at_chosen_index(self):
        self.array_list.add(10)
        self.array_list.add(20)
        self.array_list.add(30)

        self.array_list.set(1, 15)

        self.assertEqual(10, self.array_list.get(0))
        self.assertEqual(15, self.array_list.get(1))
        self.assertEqual(30, self.array_list.get(2))

    def test_can_get_array_list_size(self):
        self.array_list.add(10)
        self.array_list.add(20)

        self.assertEqual(2, self.array_list.size())

    def test_can_get_single_element_from_array_list(self):
        self.array_list.add(5)

        self.assertEqual(5, self.array_list.get(0))

    def test_can_get_multiple_elements_from_array_list(self):
        self.array_list.add(10)
        self.array_list.add(20)
        self.array_list.add(30)

        self.assertEqual(10, self.array_list.get(0))
        self.assertEqual(20, self.array_list.get(1))
        self.assertEqual(30, self.array_list.get(2))

    def test_array_list_contains_element(self):
        self.array_list.add(5)
        self.array_list.add(10)
        self.array_list.add(15)

        self.assertTrue(self.array_list.contains(10))

    def test_array_list_does_not_contain_element(self):
        self.array_list.add(5)
        self.array_list.add(10)
        self.array_list.add(15)

        self.assertFalse(self.array_list.contains(20))

    def test_can_get_first_element(self):
        self.array_list.add(5)
        self.array_list.add(10)
        self.array_list.add(15)

        self.assertEqual(5, self.array_list.get_first())

    def test_get_first_on_empty_array_list_throws_exception(self):
        with self.assertRaises(ValueError):
            self.array_list.get_first()

    def test_can_get_last_element(self):
        self.array_list.add(5)
        self.array_list.add(10)
        self.array_list.add(15)

        self.assertEqual(15, self.array_list.get_last())

    def test_get_last_on_empty_array_list_throws_exception(self):
        with self.assertRaises(ValueError):
            self.array_list.get_last()

    def test_get_index_of_element(self):
        self.array_list.add(5)
        self.array_list.add(10)
        self.array_list.add(15)

        self.assertEqual(1, self.array_list.index_of(10))


if __name__ == "__main__":
    unittest.main()