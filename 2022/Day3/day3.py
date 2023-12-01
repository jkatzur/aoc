import unittest

# Part 1
def process_file_pt1(file: str) -> int:
    with open(file) as f:
        data = f.read().splitlines()
    rows = len(data)
    width = len(data[0])

    counter = [0] * width
    gamma = [0] * width
    epsilon = [0] * width

    # Scan through each row
    # Add the 1s to each position

    for row in data:
        for i in range(width):
            counter[i] += int(row[i])

    for i in range(width):
        if counter[i] > rows // 2:
            gamma[i] = 1
        else:
            epsilon[i] = 1
    
    return int(''.join(map(str, gamma)), 2) * int(''.join(map(str, epsilon)), 2)


# Part 2
def process_file_pt2(file: str) -> int:
    with open(file) as f:
        data = f.read().splitlines()

    rows = len(data)
    width = len(data[0])

    counter = [0] * width
    gamma = [0] * width
    epsilon = [0] * width

    # Scan through each row
    # Add the 1s to each position

    for row in data:
        for i in range(width):
            counter[i] += int(row[i])

    # Oxygen generator always takes the most common bit until there is one value


    return 0


class TestInput(unittest.TestCase):
    def test_pt_1_small_file(self):
        assert process_file_pt1('small_input') == 198, f"Part 1 expecting small_input to equal 198"

    def test_pt_2_small_file(self):
        assert process_file_pt2('small_input') == 230, f"Part 2 expecting smal_input to equal 230"


if __name__ == '__main__':
    unittest.main()
    # print(process_file_pt1('input'))
    