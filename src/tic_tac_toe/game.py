from board import Board
from player import Player


class Game:

    def __init__(self, player1: Player, player2: Player):
        self.__board = Board()
        self.__player1 = player1
        self.__player2 = player2
        self.__current_player = player1

    def get_board(self):
        return self.__board

    def get_current_player(self):
        return self.__current_player

    def switch_player(self):
        if self.__current_player == self.__player1:
            self.__current_player = self.__player2
        else:
            self.__current_player = self.__player1

    def play_turn(self):
        print(
            f"\n{self.__current_player.get_name()}'s turn "
            f"({self.__current_player.get_symbol()})"
        )

        self.__board.display()

        while True:
            row, col = self.__current_player.get_move()

            if self.__board.is_valid_move(row, col):
                self.__board.place_mark(
                    row,
                    col,
                    self.__current_player.get_symbol()
                )
                break

            print("Invalid move! That spot is either taken or out of bounds. Try again.")

    def game_over(self):
        return (
            self.__board.has_winner() is not None
            or self.__board.is_draw()
        )

    def announce_result(self):
        self.__board.display()

        winner = self.__board.has_winner()

        if winner:
            if winner == self.__player1.get_symbol():
                print(f"Congratulations! {self.__player1.get_name()} wins!")
            else:
                print(f"Congratulations! {self.__player2.get_name()} wins!")
        else:
            print("It's a draw!")

    def start(self):
        print("Welcome to Tic Tac Toe!")

        while not self.game_over():
            self.play_turn()

            if self.game_over():
                break
            self.switch_player()

        self.announce_result()