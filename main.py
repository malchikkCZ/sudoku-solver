from board import Board


def main():
    board = Board()

    choices = {
        "S": board.solve,
        "G": board.generate,
    }

    prompt = input("Do you want to (S)olve some SUDOKU or (G)enerate a new one? >>> ").upper()

    try:
        choices[prompt]()
    except KeyError:
        print("You should really make up your mind.", end=" ")
        print("Please re-run the app.\n")
  

if __name__ == "__main__":
    main()
