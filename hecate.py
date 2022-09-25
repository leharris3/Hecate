from cProfile import label
import chess
import random
import os
import sys
import chess.svg
from IPython.core.display import SVG
from chessboard import display

PIECE_VALUES = {1: 1, 2: 3,
                3: 3, 4: 5, 5: 8, 6: 0}
NEUTRAL_EVAL = 0
NEG_EVAL = -100


class Engine:

    def __init__(self, board: chess.Board):
        self.name = "Hecate"
        self.board = board

    def move(self):
        return self.evaluate()

    def evaluate(self):
        legalMoves = list(self.board.legal_moves)
        bestEval = NEG_EVAL
        canidateMoves = []

        def evaluate_r(oppBoard: chess.Board, move: chess.Move):
            oppBoard.push(move)
            oppMoves = list(oppBoard.legal_moves)
            bestOppEval = 0

            if oppBoard.is_checkmate():
                return sys.maxsize
            for oppMove in oppMoves:
                eval = NEUTRAL_EVAL
                if (oppBoard.piece_at(oppMove.to_square) != None):
                    eval = PIECE_VALUES[oppBoard.piece_at(
                        oppMove.to_square).piece_type]
                    if eval > bestOppEval:
                        bestOppEval = eval
            return bestOppEval

        for move in legalMoves:
            eval = NEUTRAL_EVAL
            self.board.push(move)
            if self.board.is_checkmate():
                return move
            self.board.pop()
            if (self.board.piece_at(move.to_square) != None):
                eval = PIECE_VALUES[self.board.piece_at(
                    move.to_square).piece_type]

            fin = self.board.fen()
            clone = chess.Board(fin)
            clone.color = chess.BLACK

            eval -= evaluate_r(clone, move)
            if eval > bestEval:
                canidateMoves = []
                canidateMoves.append(move)
                bestEval = eval
            elif eval == bestEval:
                canidateMoves.append(move)
        if len(canidateMoves) == 0:
            return random.choice(legalMoves)
        return random.choice(canidateMoves)


class Game:
    def __init__(self, board: chess.Board, engine: Engine) -> None:
        self.board = board
        self.engine = engine

    def play(self):
        userColor = self.chooseColor()
        if userColor == "White":
            while not self.board.is_game_over():
                while self.board.turn == chess.WHITE:
                    self.makeUserMove()
                self.makeEngineMove()
                self.printGame()
        else:
            while not self.board.is_game_over():
                self.makeEngineMove()
                self.printGame()
                while self.board.turn == chess.BLACK:
                    self.makeUserMove()
                self.makeUserMove()
        print("Game Over!")

    def chooseColor(self):
        if (input("Choose a Side... Black or White?: ") == "White"):
            userColor = "White"
        else:
            userColor = "Black"
        return userColor

    def makeUserMove(self):
        legalMoves = list(self.board.legal_moves)
        try:
            userInput = input("Human Turn: ")
            if userInput == "undo":
                self.board.pop().pop()
            if userInput == "stop":
                quit()
            userMove = chess.Move.from_uci(userInput)

            if userMove not in legalMoves:
                print("Illegal Move!")
            self.board.push(userMove)
        except:
            print("Illegal Move!")

    def makeEngineMove(self):
        self.board.push(self.engine.move())

    def printGame(self):
        os.system('cls||clear')
        display.start(self.board.fen())


class Main:
    def main():
        board = chess.Board()
        hecate = Engine(board)
        newGame = Game(board, hecate)
        newGame.play()
        return

    if __name__ == "__main__":
        main()
