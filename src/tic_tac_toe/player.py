class Player:

    def __init__(self, name: str, symbol: str):
        self.__name = name
        self.__symbol = symbol

    def get_name(self):
        return self.__name

    def get_symbol(self):
        return self.__symbol

    def get_move(self):
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))

                if 0 <= row <= 2 and 0 <= col <= 2:
                    return row, col

                print("Row and column must be between 0 and 2.")

            except ValueError:
                print("Please enter valid numbers.")

    def __str__(self):
        return f"{self.__name} ({self.__symbol})"