import chess
import sys
from search import find_best_move

board = chess.Board()

def handle_message(message):
  if message == "uci":
    print("id name tner-py")
    print("id author firetner")
    print("uciok")
  elif message == "isready":
    print("readyok")
  elif "ucinewgame" in message:
    pass
  elif "position startpos moves" in message:
    moves = message.split(" ")[3:]
    board.clear()
    board.set_fen(chess.STARTING_BOARD_FEN)
    for move in moves:
      board.push_uci(move)
  elif "position fen" in message:
    fen = " ".join(message.split(" ")[2:])
    board.set_fen(fen)
  elif "go" in message:
    move = find_best_move(board)
    print(f"bestmove {move}")
  elif message == "quit":
    sys.exit(0)