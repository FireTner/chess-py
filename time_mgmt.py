import time

def calc_tte(remaining_time: int, time_increment: int) -> int:
  return time.time() + remaining_time / 20 + time_increment / 2

def check_time(time_to_end: int, max_margin: int = 100) -> bool:
  return time_to_end >= time.time()