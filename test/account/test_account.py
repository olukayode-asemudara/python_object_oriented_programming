import unittest
from account.account import Account


class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account()

    def test_deposit_200_balance_should_be_200(self):
        self.account.deposit(200)

        self.assertEqual(200.0, self.account.get_balance())

    def test_deposit_negative_amount_balance_should_remain_zero(self):
        self.account.deposit(-200)

        self.assertEqual(0.0, self.account.get_balance())

    def test_withdraw_from_empty_account_balance_should_remain_zero(self):
        self.account.withdraw(200, "1234")

        self.assertEqual(0.0, self.account.get_balance())

    def test_withdraw_amount_less_than_balance(self):
        self.account.deposit(500)
        self.account.withdraw(200, "1234")

        self.assertEqual(300.0, self.account.get_balance())

    def test_withdraw_amount_greater_than_balance_with_correct_password(self):
        self.account.deposit(500)
        self.account.withdraw(700, "1234")

        self.assertEqual(500.0, self.account.get_balance())

    def test_withdraw_with_short_password_throws_exception(self):
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(100, "123")

        self.assertEqual("password too short", str(context.exception))

    def test_withdraw_with_alphanumeric_password_throws_exception(self):
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(100, "12ab")

        self.assertEqual(
            "password must contain only digits",
            str(context.exception)
        )

    def test_withdraw_without_providing_password(self):
        self.account.deposit(500)

        with self.assertRaises(ValueError):
            self.account.withdraw(700, "")

        self.assertEqual(500.0, self.account.get_balance())


if __name__ == "__main__":
    unittest.main()