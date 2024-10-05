import chess
import evaluate
from helper import INT_MIN, INT_MAX
from time_mgmt import check_time, calc_tte

def search(board: chess.Board, depth: int = 0, time_to_end: int = INT_MAX):
  if depth == 0 or board.is_game_over():
    return evaluate.evaluate(board)
  
  best_score = INT_MIN

  for move in board.legal_moves:
    board.push(move)

    score = -search(board, depth - 1, time_to_end)
    if score > best_score:
      best_score = score
    
    if check_time(time_to_end):
      board.pop()
      return best_score

    board.pop()
  
  return best_score

# Find the best move given a current board position
def find_best_move(board: chess.Board, time_to_end: int) -> str:
  best_score = INT_MIN
  best_move = chess.Move.null

  for move in board.legal_moves:
    board.push(move)

    score = -search(board, 2, time_to_end)
    if score > best_score:
      best_score = score
      best_move = move

    if check_time(time_to_end):
      board.pop()
      return best_move.uci()

    board.pop()
  
  return best_move.uci()