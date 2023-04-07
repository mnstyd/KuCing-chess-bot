import chess.engine
import random
import time

class KuCing:
    def __init__(self, difficulty):
        self.board = chess.Board()
        self.engine = chess.engine.SimpleEngine.popen_uci("stockfish-windows-2022-x86-64-avx2")
        self.difficulty = difficulty
        print("Hi, I'm KuCing! Let's play some chess.")

    def make_move(self, move):
        if move not in self.board.legal_moves:
            print("Invalid move. Please make a legal move.")
            return False
        else:
            self.board.push(move)
            return True

    def play_random_move(self):
        legal_moves = list(self.board.legal_moves)
        move = random.choice(legal_moves)
        self.board.push(move)
        return move

    def play_engine_move(self):
        result = self.engine.play(self.board, chess.engine.Limit(depth=self.difficulty))
        self.board.push(result.move)
        return result.move

    def is_game_over(self):
        return self.board.is_game_over()

    def get_board(self):
        return str(self.board)

    def __del__(self):
        self.engine.quit()

if __name__ == '__main__':
    def main():
        while True:
            difficulty = input("Please choose the difficulty level (1-10): ")
            if difficulty.isdigit() and 1 <= int(difficulty) <= 10:
                break
            else:
                print("Invalid input. Difficulty level must be between 1-10. Please try again.")
        kucing = KuCing(int(difficulty))

        print("The game has started!")

        print(kucing.get_board())
        while not kucing.is_game_over():
            user_move = input("Enter your move (e.g. e2e4): ")
            user_move = chess.Move.from_uci(user_move)

            print("KuCing is thinking...")
            time.sleep(3)

            success = kucing.make_move(user_move)
            print(f"KuCing played: {success}")
            if not success:
                continue

            print(kucing.get_board())

            if kucing.is_game_over():
                if kucing.board.is_checkmate():
                    print("Congratulations, you won!")
                    kucing.__del__()
                elif kucing.board.is_stalemate() or kucing.board.is_insufficient_material():
                    print("Good game! It's a draw!")
                    kucing.__del__()
                else:
                    print("Sorry, you lost. Don't give up!")
                    kucing.__del__()

            else:
                kucing_move = kucing.play_engine_move()
                print(f"KuCing plays {kucing_move}")
                print(kucing.get_board())

    main()