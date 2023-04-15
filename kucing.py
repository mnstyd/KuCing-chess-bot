import chess.engine
import random
import time

class KuCing:
    def __init__(self, difficulty=1):
        self.board = chess.Board()
        self.difficulty = difficulty
        self.engine = chess.engine.SimpleEngine.popen_uci("stockfish-windows-2022-x86-64-avx2")
        self.color = chess.WHITE
        self.is_player_turn = True

    def play_random_move(self):
        legal_moves = list(self.board.legal_moves)
        move = random.choice(legal_moves)
        self.board.push(move)
        return move
        

    def make_move(self, player_move):
        move = chess.Move.from_uci(player_move)
        while move not in self.board.legal_moves:
            print("Invalid move, please try again.")
            move = input("Enter your move in UCI notation (e.g. e2e4): ")
            move = chess.Move.from_uci(move)
        self.board.push(move)
        return True

    def play_engine_move(self):
        self.is_player_turn = False
        # print("KuCing is thinking...")
        result = self.engine.play(self.board, chess.engine.Limit(time=self.difficulty))
        self.board.push(result.move)
        self.is_player_turn = True
        return result.move

    def is_game_over(self):
        return self.board.is_game_over()

    def get_board(self):
        return str(self.board)

    def get_difficulty(self):
        return self.difficulty

    def change_difficulty(self, new_difficulty):
        self.difficulty = new_difficulty
        print(f"Difficulty level changed to {self.difficulty}.")

    def get_color(self):
        return self.color

    def switch_color(self):
        self.color = not self.color

    def get_player_turn(self):
        return self.is_player_turn

    def get_game_result(self):
        result = self.board.result()
        if result == "1-0":
            print("Congratulations, you won!")
        elif result == "0-1":
            print("KuCing won! Don't give up, try again!")
        else:
            print("Good game, GG!")

    def __del__(self):
        self.engine.quit()