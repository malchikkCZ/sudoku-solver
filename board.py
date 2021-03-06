import os
import sys
import time
from engine import Generator, Loader, Solver


class Board:

    def __init__(self):
        self.board = [[0 for i in range(9)] for j in range(9)]
        self.show()

    def show(self):
        os.system("cls" if os.name=="nt" else "clear")
        print("    Sudoku Solver\n")
        for r in range(9):
            prt = "  "
            if r % 3 == 0 and r != 0:
                print("    " + ("+---"*3 + "+ ")*3)
            print("    " + ("+---"*3 + "+ ")*3)
            for c in range(9):
                if c % 3 == 0 and c != 0:
                    divider = "| | "
                else:
                    divider = "| "
                if self.board[r][c] == 0:
                    filled = " "
                else:
                    filled = str(self.board[r][c])
                prt = prt + divider + filled + " "
            print(" " + str(r+1) + prt + "|")
        print("    " + ("+---"*3 + "+ ")*3)
        print("\n")
    
    def load(self):
        loader = Loader(self.board)
        self.board = loader.load_board()
        if not self.board:
            print("Please re-run the app.\n")
            sys.exit()
        self.show()
    
    def solve(self):
        self.load()
        input("Great job! To start solving press ENTER.")
        print("Working ...")
        t = time.time()
        solver = Solver(self.board)
        self.board = solver.run()
        if not self.board:
            print("I'm sorry, but this SUDOKU can't be solved.\n")
            sys.exit()
        self.show()        
        t = time.time() - t
        print(f"Your SUDOKU was solved in {t:0.2f} s.\n")
    
    def generate(self):
        t = time.time()
        generator = Generator(self.board)
        self.board = generator.run()
        self.show()
        t = time.time() - t
        print(f"Your SUDOKU was generated in {t:0.2f} s.\n")
