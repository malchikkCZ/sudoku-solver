import random


class Solver:

    def __init__(self, board, excluded=(None, None, None)):
        self.board = board
        self.excluded = excluded

    def run(self):
        self.fill()
        if not self.fill():
            return None
        return self.board

    def fill(self):
        empty = self.next_empty()
        if not empty:
            return True
        r, c = empty
        for number in self.numbers():
            if (r, c, number) == self.excluded:
                continue
            if self.is_valid(r, c, number):
                self.board[r][c] = number
                if self.fill():
                    return True
                self.board[r][c] = 0
        return False
    
    def numbers(self):
        array = list(range(1, 10))
        return array

    def next_empty(self):
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0:
                    return (r, c)
    
    def is_valid(self, r, c, number):
        # row check
        if number in self.board[r]:
            return False
        # column check
        for row in range(9):
            if number == self.board[row][c]:
                return False
        # box check
        box_row = (r // 3) * 3
        box_col = (c // 3) * 3
        for row in range(3):
            for col in range(3):
                if number == self.board[row + box_row][col + box_col]:
                    return False
        return True


class Loader(Solver):

    def __init__(self, board):
        super().__init__(board)

    def load_board(self):
        for row in range(9):
            length = 9
            answer = input(f"Enter the numbers in {row+1}. row >>> ")
            if len(answer) < length:
                length = len(answer)
            for col in range(length):
                try:
                    number = int(answer[col])
                except ValueError:
                    print("You need to enter the sequence of numbers.", end=" ")
                    return None
                if number > 0:
                    if self.is_valid(row, col, number):
                        self.board[row][col] = int(number)
                    else:
                        print("Some of the numbers can't be placed.", end=" ")
                        return None
        return self.board


class Generator(Solver):

    def __init__(self, board):
        super().__init__(board)

    def run(self):
        self.fill()
        to_hide = random.randint(30, 60)
        while to_hide > 0:
            r = random.randint(0, 8)
            c = random.randint(0, 8)
            if self.board[r][c] == 0:
                continue
            number = self.board[r][c]
            self.board[r][c] = 0
            test_board = [row.copy() for row in self.board]
            solver = Solver(test_board, excluded=(r, c, number))
            if not solver.run():
                to_hide -= 1
            else:
                self.board[r][c] = number
        return self.board
    
    def numbers(self):
        array = list(range(1, 10))
        random.shuffle(array)
        return array
