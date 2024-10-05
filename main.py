import uci

def main():
  while True:
    message = input()
    uci.handle_message(message)

if __name__ == "__main__":
  main()