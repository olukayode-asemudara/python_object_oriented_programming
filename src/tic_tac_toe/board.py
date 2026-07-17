class Board:

    def __init__(self):
        self.__grid = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

    def get_grid(self):
        return self.__grid

    def place_mark(self, row: int, col: int, symbol: str) -> bool:
        if self.is_valid_move(row, col):
            self.__grid[row][col] = symbol
            return True
        return False

    def is_valid_move(self, row: int, col: int) -> bool:
        return (
            0 <= row < 3
            and 0 <= col < 3
            and self.__grid[row][col] == " "
        )

    def check_row_win(self):
        for row in self.__grid:
            if row[0] == row[1] == row[2] != " ":
                return row[0]
        return None

    def check_column_win(self):
        for col in range(3):
            if (
                self.__grid[0][col]
                == self.__grid[1][col]
                == self.__grid[2][col]
                != " "
            ):
                return self.__grid[0][col]
        return None

    def check_diagonal_win(self):
        # Main diagonal
        if (
            self.__grid[0][0]
            == self.__grid[1][1]
            == self.__grid[2][2]
            != " "
        ):
            return self.__grid[0][0]

        # Secondary diagonal
        if (
            self.__grid[0][2]
            == self.__grid[1][1]
            == self.__grid[2][0]
            != " "
        ):
            return self.__grid[0][2]

        return None

    def has_winner(self):
        return (
            self.check_row_win()
            or self.check_column_win()
            or self.check_diagonal_win()
        )

    def is_draw(self):
        if self.has_winner():
            return False

        for row in self.__grid:
            if " " in row:
                return False

        return True

    def reset(self):
        self.__grid = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

    def display(self):
        print(self)

    def __str__(self):
        rows = []

        for row in self.__grid:
            rows.append(" " + " | ".join(row) + " ")

        return "\n---+---+---\n".join(rows)