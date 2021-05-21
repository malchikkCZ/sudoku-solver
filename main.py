from board import Board
import time

board = Board()
board.show()

board.load()
board.show()

input("Great job! To start solving press ENTER.")
print("Working ...")

t = time.time()
board.solve()
t = time.time() - t

board.show()
print(f"Your SUDOKU was solved in {t:0.2f} s.\n")
