import chess


class Engine:
    def __init__(self):
        self.name = "Hectate"
        # ...
        return


class Game:
    def __init__(self, board, engine) -> None:
        self.board = board
        self.engine = engine

    def play(self):
        userColor = self.chooseColor()
        while not self.board.is_game_over():
            print("the game goes on...")
            return

    def chooseColor(self):
        if (input("Choose a Side... Black or White?: ") == "White"):
            userColor = "White"
        else:
            userColor = "Black"
        return userColor


class Main:
    def main():
        hectate = Engine()
        newGame = Game(chess.Board(), hectate)
        newGame.play()

        test = chess.Board()
        test.is_game_over
        return

    if __name__ == "__main__":
        main()
