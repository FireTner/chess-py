import uci
import logging

logging.basicConfig(
  filename="app.log",
  encoding="utf-8",
  filemode="w",
  format="{asctime} - {levelname} - {message}",
  style="{",
  datefmt="%Y-%m-%d %H:%M",
  level=logging.DEBUG,
)

def main():
  logging.info("Started")
  try:
    while True:
      message = input()
      logging.info(f"> {message}")
      uci.handle_message(message)
  except Exception as e:
    logging.error(f"error {repr(e)}; ", exc_info=True, stack_info=True)


if __name__ == "__main__":
  main()