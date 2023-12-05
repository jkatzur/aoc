def count_games(game_inputs, max_hash, count_fn):
    total = 0
    for count,roundg in enumerate(game_inputs):
        total += count_fn(count+1, roundg, max_hash)
    return total

def count_game(index, roundg, max_hash):
    total = 0
    for game in roundg.split(':')[1].split(';'):
        for roll in game.split(','):
            for color in ('green', 'red', 'blue'):
                if roll.find(color) != -1:
                    if int(roll[0:roll.find(color)]) > max_hash[color]:
                        return 0;
    return index;

def power_game(index, roundg, max_hash):
    mins = {'blue': 1, 'red': 1, 'green': 1}
    for game in roundg.split(':')[1].split(';'):
        for roll in game.split(','):
            for color in ('green', 'red', 'blue'):
                if roll.find(color) != -1:
                    mins[color] = max(mins[color], int(roll[0:roll.find(color)]))
    return mins['blue'] * mins['green'] * mins['red']

def read_input():
    f = open("input2.txt", "r")
    return f.readlines()

def day1():
    print(count_games(read_input(), {'green': 13, 'red': 12, 'blue': 14}, count_game))

def day2():
    print(count_games(read_input(), {'green': 13, 'red': 12, 'blue': 14}, power_game))

if __name__ == '__main__':
    day2()