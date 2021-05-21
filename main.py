import os
import sys
import time


def cls():
  os.system('cls' if os.name=='nt' else 'clear')


def show_sudoku():
  cls()
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
      if table[r][c] == 0:
        filled = " "
      else:
        filled = str(table[r][c])
      prt = prt + divider + filled + " "
    print(" " + str(r+1) + prt + "|")
  print("    " + ("+---"*3 + "+ ")*3)
  print("\n")


def solve():
  empty = next_empty()
  if not empty:
    return True
  r, c = empty
  for number in range(1,10):
    if is_valid(r, c, number):
      table[r][c] = number
      if solve():
        return True
      table[r][c] = 0
  return False


def next_empty():
  for r in range(9):
    for c in range(9):
      if table[r][c] == 0:
        return (r, c)


def is_valid(r, c, number):
  # row check
  if number in table[r]:
    return False
  # column check
  for row in range(9):
    if number == table[row][c]:
      return False
  # box check
  box_row = (r // 3) * 3
  box_col = (c // 3) * 3
  for row in range(3):
    for col in range(3):
      if number == table[row + box_row][col + box_col]:
        return False
  return True


error = "Please re-run the app."
table = [[0 for i in range(9)] for j in range(9)]

show_sudoku()

for row in range(9):
  length = 9
  answer = input(f"Enter the nuber in {row+1}. row >>> ")
  if len(answer) < length:
    length = len(answer)
  for col in range(length):
    try:
      number = int(answer[col])
    except ValueError:
      print("You need to enter the sequence of numbers. " + error)
      sys.exit()
    if number > 0:
      if is_valid(row, col, number):
        table[row][col] = int(number)
      else:
        print("Some of the numbers can't be placed. " + error)
        sys.exit()

  show_sudoku()

input("Great job! To start solving press ENTER.")
print("Working ...")
t = time.perf_counter()

solve()
t = time.perf_counter() - t

if solve():
  show_sudoku()
  print(f"Your SUDOKU was solved in {t:0.2f} s.\n")
else:
  show_sudoku()
  print("I'm sorry, but this SUDOKU can't be solved.\n")
