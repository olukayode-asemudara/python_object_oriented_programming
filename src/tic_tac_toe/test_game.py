import unittest

from tic_tac_toe.board import Board
from .player import Player

class TicTacToe(unittest.TestCase):

    def test_create_players(self):
        player_one = Player("Kay", "X")
        player_two = Player("Jane", "O")
        self.assertIsNotNone(player_one)
        self.assertIsNotNone(player_two)

    def test_switch_player_changes_turn(self):
        player_one = Player("Kay", "X")
        player_two = Player("Jane", "O")
        from tic_tac_toe.game import Game
        game = Game(player_one, player_two)
        self.assertIs(game.get_current_player(), player_one)
        game.switch_player()
        self.assertIs(game.get_current_player(), player_two)

    def test_board_place_mark_and_detect_row_winner(self):
        board = Board()
        board.place_mark(0, 0, "X")
        board.place_mark(0, 1, "X")
        board.place_mark(0, 2, "X")
        self.assertEqual(board.get_grid()[0][0], "X")
        self.assertEqual(board.has_winner(), "X")

    def test_board_rejects_invalid_or_duplicate_moves(self):
        board = Board()
        self.assertTrue(board.is_valid_move(1, 1))
        board.place_mark(1, 1, "X")
        self.assertFalse(board.is_valid_move(1, 1))
        self.assertFalse(board.place_mark(1, 1, "O"))
        self.assertFalse(board.is_valid_move(3, 1))
        self.assertFalse(board.is_valid_move(-1, 0))

    def test_board_detects_column_win(self):
        board = Board()

        board.place_mark(0, 1, "O")
        board.place_mark(1, 1, "O")
        board.place_mark(2, 1, "O")

        self.assertEqual(board.check_column_win(), "O")
        self.assertEqual(board.has_winner(), "O")

    def test_board_detects_draw(self):
        board = Board()
        draw_grid = [
            ["X", "O", "X"],
            ["X", "O", "O"],
            ["O", "X", "X"]
        ]

        for row in range(3):
            for col in range(3):
                board.place_mark(row, col, draw_grid[row][col])
        self.assertFalse(board.has_winner())
        self.assertTrue(board.is_draw())


if __name__ == "__main__":
    unittest.main()