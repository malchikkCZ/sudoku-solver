class Solver:

    def __init__(self, board):
        self.board = board

    def run(self):
        self.solve()
        if not self.solve():
            return None
        return self.board

    def solve(self):
        empty = self.next_empty()
        if not empty:
            return True
        r, c = empty
        for number in range(1, 10):
            if self.is_valid(r, c, number):
                self.board[r][c] = number
                if self.solve():
                    return True
                self.board[r][c] = 0
        return False

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
