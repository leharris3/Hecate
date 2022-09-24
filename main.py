import chess
import random
import os


class Engine:
    def __init__(self, board: chess.Board):
        self.name = "Hectate"
        self.board = board

    def move(self):
        move_list = list(self.board.legal_moves)
        random_move = random.choice(move_list)
        return random_move


class Game:
    def __init__(self, board: chess.Board, engine: Engine) -> None:
        self.board = board
        self.engine = engine

    def play(self):
        userColor = self.chooseColor()
        if userColor == "White":
            while not self.board.is_game_over():
                self.makeUserMove()
                self.makeEngineMove()
                self.printGame()
        else:
            while not self.board.is_game_over():
                self.makeEngineMove()
                self.printGame()
                self.makeUserMove()

    def chooseColor(self):
        if (input("Choose a Side... Black or White?: ") == "White"):
            userColor = "White"
        else:
            userColor = "Black"
        return userColor

    def makeUserMove(self):
        self.board.push(chess.Move.from_uci(input("Human Turn: ")))

    def makeEngineMove(self):
        self.board.push(self.engine.move())

    def printGame(self):
        os.system('cls||clear')
        print(self.board)


class Main:
    def main():
        board = chess.Board()
        hectate = Engine(board)
        newGame = Game(board, hectate)
        newGame.play()
        return

    if __name__ == "__main__":
        main()
