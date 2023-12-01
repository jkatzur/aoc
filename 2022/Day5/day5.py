import unittest

class Board():
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
        self.board = [[0] * self.x for _ in range(self.y)]

    def print_board(self):
        for r in self.board:
            print(r)
        print("----------------------------------------")

    def add_line(self, first: tuple, second: tuple, pt2: bool = False):
        first_x, first_y = first
        second_x, second_y = second
        # figure out if this is horizontal or vertical
        if first_x == second_x:
            # vertical
            if second_y > first_y:
                for y in range(first_y, second_y + 1):
                    self.board[y][first_x] += 1
            else:
                for y in range(second_y, first_y + 1):
                    self.board[y][first_x] += 1
            # horizontal
        elif first_y == second_y:
            if second_x > first_x:
                for x in range(first_x, second_x+1):
                    self.board[first_y][x] += 1
            else:
                for x in range(second_x, first_x+1):
                    self.board[first_y][x] += 1

        # Add y=x diaganol
        elif pt2 and ((first_y-second_y) == (first_x-second_x)):
            if second_y > first_y:
                for i in range(0, (second_y - first_y + 1)):
                    self.board[first_y+i][first_x+i] += 1
            else:
                for i in range(0, (first_y - second_y + 1)):
                    self.board[second_y+i][second_x+i] += 1

        # Add y = -x diaganol
        elif pt2 and (abs(first_y-second_y) == abs(first_x-second_x)):
            if second_y > first_y:
                for i in range(0, (second_y-first_y + 1)):
                    self.board[first_y+i][first_x-i] += 1
            else:
                for i in range(0, (first_y - second_y+1)):
                    self.board[second_y+i][second_x-i] += 1


    def calculate_points(self) -> int:
        total = 0
        for r in self.board:
            for c in r:
                if c > 1:
                    total += 1
        return total

def read_from_file(file:str, x:int, y:int, pt2: bool = False) -> int:
    newBoard = Board(x,y)
    with open(file) as f:
        data = f.read().splitlines()
    
    for row in data:
        first_x, first_y = (int(f) for f in row.split(" -> ")[0].split(','))
        second_x, second_y = (int(s) for s in row.split(" -> ")[1].split(','))
        newBoard.add_line((first_x, first_y), (second_x, second_y), pt2)

    return newBoard.calculate_points()

class TestInput(unittest.TestCase):
    def test_pt_1_small_input(self):
        assert read_from_file('small_input',10,10) == 5, f"Part 1 expecting small_input to equal 5"

    def test_pt_1_input(self):
        assert read_from_file('input',1000,1000) == 7468, f"Part 1 expecting input to equal 7468"

    def test_pt_2_small_input(self):
        assert read_from_file('small_input',10,10, True) == 12, f"Part 2 expecting small_input to equal 12"

    def test_pt_2_input(self):
        assert read_from_file('input',1000,1000, True) == 22364, f"Part 2 expecting small_input to equal 12"


if __name__ == '__main__':
    unittest.main()
    # newBoard = Board(10,10)
    # newBoard.print_board()
    # newBoard.add_line((0,9), (5,9))
    # newBoard.add_line((8,0), (0,8))
    # newBoard.add_line((0,9), (2,9))
    # newBoard.print_board()
    # print(newBoard.calculate_points())
    # print(read_from_file('small_input'))

    #print(read_from_file('small_input', 10, 10, True))

    #print(read_from_file('input', 1000, 1000, True))