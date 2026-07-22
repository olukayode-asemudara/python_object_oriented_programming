class Account:
    def __init__(self):
        self.balance = 0.0

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount, password):
        if password is None:
            raise ValueError("password field is empty")

        if len(password) < 4:
            raise ValueError("password too short")

        if not password.isdigit():
            raise ValueError("password must contain only digits")

        if amount <= self.balance:
            self.balance -= amount