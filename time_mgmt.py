import time

def calc_tte(remaining_time: int) -> int:
  return time.time() + remaining_time

def check_time(time_to_end: int, max_margin: int = 100) -> bool:
  return (time_to_end - time.time()) < max_margin