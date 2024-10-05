import chess
import evaluate
from helper import INT_MIN, INT_MAX

def search(board: chess.Board, depth = 0):
  if depth == 0 or board.is_game_over():
    return evaluate.evaluate(board)
  
  best_score = INT_MIN
  best_move = chess.Move.null

  for move in board.legal_moves:
    board.push(move)

    score = -search(depth - 1)
    if score > best_score:
      best_score = score
      best_move = move

    board.pop()
  
  return best_move, best_score

# Find the best move given a current board position
def find_best_move(board: chess.Board):
  search(board, 2)