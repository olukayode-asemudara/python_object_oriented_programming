from player import Player
from game import Game


def main():

    print("===== TIC TAC TOE =====")

    player1_name = input("Enter Player One Name: ")
    player2_name = input("Enter Player Two Name: ")

    player1 = Player(player1_name, "X")
    player2 = Player(player2_name, "O")

    game = Game(player1, player2)

    game.start()


if __name__ == "__main__":
    main()