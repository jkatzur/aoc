def count_games(game_inputs, max_hash):
    total = 0
    for count,roundg in enumerate(game_inputs):
        total += count_game(count+1, roundg, max_hash)
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

f = open("input2.txt", "r")
lines = f.readlines()

print(count_games(lines, {'green': 13, 'red': 12, 'blue': 14}))