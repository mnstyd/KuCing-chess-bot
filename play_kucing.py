import os
import sys
import time

from kucing import KuCing
import chess

def main():
    print("Hi, I'm KuCing! Let's play some chess.")
    while True:
        try:
            difficulty = int(input("Please choose the difficulty level (1-10): "))
            if difficulty < 1 or difficulty > 10:
                print("Please enter a number between 1 and 10.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")
    
    board = chess.Board()
    kucing = KuCing(difficulty)
    time.sleep(1)
    print("\nHello! I'm KuCing and I'll be playing against you in this game of chess.")
    time.sleep(1)
    print(f"KuCing's difficulty level is set to {difficulty}. Good luck and have fun!")
    time.sleep(1)
    print("KuCing plays as black. You play as white. Let's start!\n")
    time.sleep(1)
    
    while not board.is_game_over():
        print("Current board:\n", board)
    
        while True:
            player_move = input("Enter your move in UCI notation (e.g. e2e4): ")
        
            if player_move.lower() == "resign":
                print("You resigned! Better luck next time!")
                sys.exit(0)
            
            try:
                move = chess.Move.from_uci(player_move)
                if move in board.legal_moves:
                    break
                else:
                    print("Invalid move. Please enter a valid move.")
            except ValueError:
                print("Invalid move. Please enter a valid move. (e.g. e2e4):")
    
        board.push(move)
    
        print(f"\nKuCing is thinking...")
        kucing_move = kucing.play_engine_move()
        while kucing_move not in board.legal_moves:
            kucing_move = kucing.play_engine_move()
        print(f"KuCing played: {kucing_move}\n")
        board.push(kucing_move)
    
        if board.is_game_over():
            result = board.result()
            print("\nFinal board:\n", board)
            if result == "1-0":
                print("Congratulations! You won the game!")
                kucing.congratulate()
            elif result == "0-1":
                print("Sorry, you lost the game.")
                kucing.motivate()
            else:
                print("The game ended in a draw. Good game!")
                kucing.good_game()
            break

if __name__ == '__main__':
    main()