import chess
import sys
from search import find_best_move

board = chess.Board()

def handle_message(message):
  split_message = message.split(" ")
  if message == "uci":
    print("id name tner-py")
    print("id author firetner")
    print("uciok")
  elif message == "isready":
    print("readyok")
  elif "ucinewgame" in message:
    pass
  elif "position startpos moves" in message:
    moves = split_message[3:]
    board.clear()
    board.set_fen(chess.STARTING_BOARD_FEN)
    for move in moves:
      board.push_uci(move)
  elif "position fen" in message:
    fen = " ".join(split_message[2:])
    board.set_fen(fen)
  elif split_message[0] == "go":
    assert split_message[1] == "wtime"
    wtime = int(split_message[2])
    assert split_message[3] == "btime"
    btime = int(split_message[4])
    move = find_best_move(board, wtime if board.turn else btime)
    print(f"bestmove {move}")
  elif message == "quit":
    sys.exit(0)