import chess.engine
import random

class KuCing:
    def __init__(self):
        self.board = chess.Board()
        self.engine = chess.engine.SimpleEngine.popen_uci("stockfish-windows-2022-x86-64-avx2")

    def make_move(self, move_string):
        try:
            move = chess.Move.from_uci(move_string)
            if move not in self.board.legal_moves:
                print("Invalid move. Please make a legal move.")
                return False
            else:
                self.board.push(move)
                return True
        except ValueError:
            print("Invalid move format. Please enter your move in the format 'e2e4'.")
            return False

    def play_random_move(self):
        legal_moves = list(self.board.legal_moves)
        move = random.choice(legal_moves)
        self.board.push(move)
        return move

    def play_engine_move(self):
        result = self.engine.play(self.board, chess.engine.Limit(time=2.0))
        self.board.push(result.move)
        return result.move

    def is_game_over(self):
        return self.board.is_game_over()

    def get_board(self):
        return str(self.board)

    def __del__(self):
        self.engine.quit()