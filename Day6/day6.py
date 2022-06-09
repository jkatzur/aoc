from typing import List
import unittest

def day(starter: List[int]) -> List[int]:
    # 3,4,3,1,2
    temp = starter[:]
    for i, fish in enumerate(temp):
        if fish == 0:
            starter.append(8)
            starter[i] = 6
        else:
            starter[i] -= 1
    
    return starter

def sim(turns: int, starter:List[int]) -> int:
    turn = 0
    lantern_fish = starter
    while turn < turns:
        lantern_fish = day(lantern_fish)
        turn += 1
    return len(lantern_fish)

def day_counter(counter:List[int]) -> List[int]:
    temp = counter[:]
    temp[8] = counter[0]
    temp[0] = counter[1]
    temp[1] = counter[2]
    temp[2] = counter[3]
    temp[3] = counter[4]
    temp[4] = counter[5]
    temp[5] = counter[6]
    temp[6] = counter[7] + counter[0]
    temp[7] = counter[8]
    return temp

def classify(turns:int, starter:List[int]) -> int:
    counter = [0] * 9
    for fish in starter:
        counter[fish] += 1

    turn = 0
    while turn < turns:
        counter = day_counter(counter)
        turn += 1

    return sum(counter)

    # 5...
    # 5 turns... 1 fish (0)
    # 6 turns... 2 fish (6, 8)
    # 12 turns... 2 fish (0, 2)
    # 13 turns... 3 fish (6, 1, 8)
    # 15 turns... 4 fish (4, 6, 6, 8)
    # 20 turns... 5 fish (6, 1, 1, 3, 8)

class TestInput(unittest.TestCase):
    def test_pt_1_18(self):
        assert sim(18, [3,4,3,1,2]) == 26, f"Part 1 expecting 18 to equal 26"

    def test_pt_1_80(self):
        assert sim(80, [3,4,3,1,2])== 5934, f"Part 1 expecting 80 to equal 5934"

    def test_pt_2_256_small(self):
        assert classify(256, [3,4,3,1,2]) == 26984457539, f"Part 2 expecting 256 to equal 26984457539"

if __name__=='__main__':
    unittest.main()
    # print(classify(256, [1,1,3,5,1,1,1,4,1,5,1,1,1,1,1,1,1,3,1,1,1,1,2,5,1,1,1,1,1,2,1,4,1,4,1,1,1,1,1,3,1,1,5,1,1,1,4,1,1,1,4,1,1,3,5,1,1,1,1,4,1,5,4,1,1,2,3,2,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,5,1,1,1,3,4,1,1,1,1,3,1,1,1,1,1,4,1,1,3,1,1,3,1,1,1,1,1,3,1,5,2,3,1,2,3,1,1,2,1,2,4,5,1,5,1,4,1,1,1,1,2,1,5,1,1,1,1,1,5,1,1,3,1,1,1,1,1,1,4,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,3,2,1,1,1,1,2,2,1,2,1,1,1,5,5,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,4,2,1,4,1,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,5,1,1,1,1,1,1,1,1,3,1,1,3,3,1,1,1,3,5,1,1,4,1,1,1,1,1,4,1,1,3,1,1,1,1,1,1,1,1,2,1,5,1,1,1,1,1,1,1,1,1,1,4,1,1,1,1]))