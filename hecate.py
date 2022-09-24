import chess
import random
import os
import sys
import chess.svg
from IPython.core.display import SVG


PIECE_VALUES = {1: 1, 2: 3,
                3: 3, 4: 5, 5: 8, 6: 0}
NEUTRAL_EVAL = 0


class Engine:

    def __init__(self, board: chess.Board):
        self.name = "Hecate"
        self.board = board

    def move(self):
        return self.evaluate()

    def evaluate(self):
        legalMoves = list(self.board.legal_moves)
        bestEval = NEUTRAL_EVAL
        canidateMoves = legalMoves

        def evaluate_r(oppBoard: chess.Board, move: chess.Move):
            oppBoard.push(move)
            oppMoves = list(oppBoard.legal_moves)
            bestOppEval = NEUTRAL_EVAL

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

            if move != None:
                eval -= evaluate_r(clone, move)

            if eval > bestEval:
                canidateMoves = []
                canidateMoves.append(move)
                bestEval = eval
            elif eval == bestEval:
                canidateMoves.append(move)

            return random.choice(canidateMoves)


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
        print("Game Over!")

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
        hecate = Engine(board)
        newGame = Game(board, hecate)
        newGame.play()
        return

    if __name__ == "__main__":
        main()
