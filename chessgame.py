import chess

board = chess.Board()

while not board.is_game_over():
    print(board)
    move = input("Enter your move (e.g. e2e4): ")
    try:
        board.push_san(move)
    except ValueError:
        print("Invalid move, try again.")