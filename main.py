# Aplikaci Sudoku Solver naprogramoval Malchikk.CZ (C) 2021-03-30

import sys
import os
import time

def cls():
  '''Tato funkce smaze obrazovku v ruznych OS.'''
  os.system('cls' if os.name=='nt' else 'clear')

def show_sudoku():
  '''Tato funkce vykresli na obrazovku tabulku s hodnotami v sudoku.'''
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
        filled = " "                                      # pokud je na danem miste 0, vytiskne se prazdne pole
      else:
        filled = str(table[r][c])                         # jinak se vytiskne cislo, ktere do bunky patri
      prt = prt + divider + filled + " "
    print(" " + str(r+1) + prt + "|")
  print("    " + ("+---"*3 + "+ ")*3)
  print("\n")

def solve():
  '''Tato funkce predstavuje algoritmus pro hledani reseni.'''
  empty = next_empty()                                    # najde dalsi pole, ktere jeste nebylo vyplneno
  if not empty:                                           # pokud uz takove misto neni, je sudoku vyresene
    return True
  r = empty[0]
  c = empty[1]                                            # prevede souradnice na samostatne promenne
  for number in range(1,10):                              # postupne bude zkouset vyplnovat jednotliva cisla od 1 do 9
    if is_valid(r, c, number):                            # pokud umisteni cisla odpovida pravidlum
      table[r][c] = number                                # zapise se do tabulky sudoku
      if solve():                                         # pokud bylo predchozi pole uspesne vyreseno, pokracuje na dalsi
        return True
      table[r][c] = 0                                     # jinak oznaci pole jako prazdne
  return False                                            # a vrati se na predchozi pole
  
def next_empty():
  '''Tato funkce najde dalsi prazdne misto v tabulce.'''
  for r in range(9):                                      # pro kazdy radek
    for c in range(9):                                    # a pro kazdy sloupec
      if table[r][c] == 0:                                # pokud je pole prazdne
        return (r, c)                                     # vrati jeho souradnice

def is_valid(r, c, number):
  '''Tato funkce overi, zda na danem miste muze byt konkretni cislo.'''
  # row check
  if number in table[r]:                                  # overi cislo v danem radku
    return False
  # column check
  for row in range(9):                                    # overi cislo v danem sloupci
    if number == table[row][c]:
      return False
  # box check
  box_row = (r // 3) * 3                                  # urci kolikaty box v rade
  box_col = (c // 3) * 3                                  # a kolikaty box ve sloupci
  for row in range(3):                                    # overi cislo v danem boxu
    for col in range(3):
      if number == table[row + box_row][col + box_col]:
        return False
  return True                                             # pokud cislo projde vsemi testy, pouzije se jako reseni

error = "Spustte program znovu a zacnete od zacatku."
table = [[0 for i in range(9)] for j in range(9)]         # urci prazdnou tabulku sudoku
show_sudoku()                                             # a vykresli ji na obrazovku

for row in range(9):                                      # pro kazdou radu v tabulce
  length = 9
  answer = input(f"Zadej cisla na {row+1}. radku >>> ")   # bude ocekavat vstup od uzivatele
  if len(answer) < length:                                # pokud ma odpoved vice nez 9 znaku, budou se dalsi znaky ignorovat
    length = len(answer)
  for col in range(length):                               # postupne bude zpracovavat zadane znaky
    try:
      number = int(answer[col])                           # prevede dany znak na cislo
    except ValueError:
      print("Zadanim muze byt pouze rada cisel. " + error)
      sys.exit()                                          # pokud se to nepovede, vypise chybu a ukonci program
    if number > 0:                                        # pokud je dane cislo vetsi nez 0
      if is_valid(row, col, number):                      # overi, zda muze na danem miste vubec byt
        table[row][col] = int(number)                     # a zapise ho do tabulky sudoku
      else:
        print("Nektere z cisel nelze umistit. " + error)  # v opacnem pripade vypise chybu a ukonci program
        sys.exit()

  show_sudoku()                                           # po kazdem zadanem radku vypise na obrazovku tabulku s jiz vyplnenymi hodnotami

input("Vyborne! Lusteni spustite klavesou ENTER.")
print("Pracuji ...")
t = time.perf_counter()                                   # spusti casomiru

solve()                                                   # spusti algoritmus pro vyhledavani reseni
t = time.perf_counter() - t                               # vypne casomiru

if solve():                                               # pokud program uspesne vyplnil vsechna pole
  show_sudoku()
  print(f"Vase SUDOKU bylo vylusteno za {t:0.2f} s.\n")    # vypise vysledek na obrazovku
else:                                                     # pokud program nenasel spravne reseni
  show_sudoku()
  print("Je mi lito, ale toto SUDOKU nema reseni.\n")    # da o tom zpravu uzivateli


