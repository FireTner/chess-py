import chess
import sys
from search import find_best_move
from time_mgmt import calc_tte
import logging

board = chess.Board()

def handle_message(message):
  split_message = message.split(" ")
  if message == "uci":
    logging.debug("uci decoded")
    print("id name tner-py")
    print("id author firetner")
    print("uciok")
  elif "isready" in message:
    logging.debug("isready decoded")
    print("readyok")
  elif "ucinewgame" in message:
    logging.debug("ucinewgame decoded")
    pass
  elif "position startpos moves" in message:
    logging.debug("position startpos decoded")
    moves = split_message[3:]
    board.clear()
    board.set_fen(chess.STARTING_FEN)
    for move in moves:
      board.push_uci(move)
  elif "position fen" in message:
    logging.debug("position fen decoded")
    fen = " ".join(split_message[2:])
    board.set_fen(fen)
  elif split_message[0] == "go":
    logging.debug("go decoded")
    arguments = {
      "wtime": 0,
      "btime": 0,
      "winc": 0,
      "binc": 0,
    }

    i = 1
    while i < len(split_message):
      if split_message[i] in arguments:
        if i + 1 == len(split_message):
          break
        arguments[split_message[i]] = int(split_message[i + 1])
        i += 1

      i += 1
    
    wtime = arguments["wtime"]
    btime = arguments["btime"]
    winc = arguments["winc"]
    binc = arguments["binc"]

    move = find_best_move(board, calc_tte(wtime, winc) if board.turn else calc_tte(btime, binc))
    print(f"bestmove {move}")
  elif message == "quit":
    logging.debug("quit decoded")
    sys.exit(0)
  else:
    logging.debug("unknown message")