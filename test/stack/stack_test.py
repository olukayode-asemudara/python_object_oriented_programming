import unittest
from stack.stack import Stack

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_new_stack_is_empty(self):
        self.assertTrue(self.stack.is_empty())

    def test_push_x_stack_is_not_empty(self):
        self.stack.push("Merlin")
        self.assertFalse(self.stack.is_empty())

    def test_push_x_pop_x_stack_is_empty(self):
        self.stack.push("Merlin")
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def test_push_x_pop_returns_x(self):
        self.stack.push("Don paps")
        self.assertEqual("Don paps", self.stack.pop())

    def test_push_xy_pop_twice_stack_is_empty(self):
        self.stack.push("Don")
        self.stack.push("Paps")

        self.stack.pop()
        self.stack.pop()

        self.assertTrue(self.stack.is_empty())

    def test_push_xy_pop_once_stack_is_not_empty(self):
        self.stack.push("Don")
        self.stack.push("Paps")

        self.stack.pop()

        self.assertFalse(self.stack.is_empty())

    def test_push_xy_pop_twice_returns_yx(self):
        self.stack.push("Don")
        self.stack.push("Paps")

        self.assertEqual("Paps", self.stack.pop())
        self.assertEqual("Don", self.stack.pop())

    def test_push_xy_pop_thrice_throws_exception(self):
        self.stack.push("Don")
        self.stack.push("Paps")

        self.stack.pop()
        self.stack.pop()

        with self.assertRaises(ValueError):
            self.stack.pop()

    def test_push_xyz_peek_returns_z(self):
        self.stack.push("Don")
        self.stack.push("Paps")
        self.stack.push("Guinevere")

        self.assertEqual("Guinevere", self.stack.peek())

    def test_peek_on_empty_stack_throws_exception(self):
        with self.assertRaises(ValueError):
            self.stack.peek()

if __name__ == "__main__":
    unittest.main()