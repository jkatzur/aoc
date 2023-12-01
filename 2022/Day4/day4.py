import unittest

class Board:
    def __init__(self) -> None:
        self.board = [[0] * 5 for i in range(5)]
        self.marked = [[0] * 5 for i in range(5)]

    def add_row(self, row, row_num):
        # figured out this was fixed with... using int() to handle whitespace
        self.board[row_num] = [int(row[3*x:3*x+3]) for x in range(0,5)]

    def print(self):
        for r in self.board:
            print(r)

    def print_marks(self):
        for r in self.marked:
            print(r)

    def did_win(self):
        for i in range(5):
            # Check each row
            if sum(self.marked[i]) == 5:
                return True
            # Check columns
            elif (self.marked[0][i] + self.marked[1][i] + self.marked[2][i] + self.marked[3][i] + self.marked[4][i]) == 5:
                return True
            # Not rules say no diagonals
        return False

    def mark(self, num):
        # figure out if num is in the board
        # if it is update the self.marked to 1 in that position
        for r in range(5):
            for c in range(5):
                if self.board[r][c] == num:
                    self.marked[r][c] = 1

    def score(self):
        # build list of non-marked... then sum the values
        return sum(self.board[r][c] for r in range(5) for c in range(5) if self.marked[r][c] == 0)

def run_game(file):
    called_nums, boards = prep_game(file)
    for num in called_nums:
        # For each number let's mark every board
        # then let's check every board for win
            # if there's a win let's stop
        for board in boards:
            board.mark(int(num))
            if board.did_win():
                return board.score() * num

def last_board(file):
    called_nums, boards = prep_game(file)
    alive_indexes = [i for i in range(len(boards))] # create a list of alive indexes
    for num in called_nums:
        for i in alive_indexes[:]: # create a copy of the list of alive indexes each run so we can remove the original array
            boards[i].mark(int(num))
            if boards[i].did_win():
                if len(alive_indexes) == 1:
                    return boards[i].score() * num # if the last board wins return the score
                alive_indexes.remove(i) # if a board wins remove it from future loops


def prep_game(file):
    with open(file) as f:
        data = f.read().splitlines()
    
    called_nums = [int(x) for x in data[0].split(',')]
    boards = []
    for line in data[1:]:
        if line == '':
            curr_board = Board()
            i = 0
        else:
            curr_board.add_row(line, i)
            if i == 4:
                boards.append(curr_board)
            i += 1
    return (called_nums, boards)


class TestInput(unittest.TestCase):
    def test_pt_1_small_file(self):
        assert run_game('small_input.txt') == 4512, f"Part 1 expecting small_input to equal 4512"

    def test_pt_2_small_file(self):
        assert last_board('small_input.txt') == 1924, f"Part 2 expecting small_input to equal 1924"


if __name__ == '__main__':
    unittest.main()
    # print(run_game('input.txt'))
    # print(last_board('input.txt'))