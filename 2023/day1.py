def day1():
    f = open("input.txt", "r")
    lines = f.readlines()
    print(sum(int([c for c in row if c.isnumeric()][0] + [c for c in row if c.isnumeric()][-1]) for row in lines))

def day2():
    from collections import defaultdict
    f = open("input.txt", "r")
    lines = f.readlines()
    alpha_values = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    alpha_map = defaultdict(list)
    for alpha in alpha_values.keys():
        alpha_map[alpha[0]].append(alpha)

    def translate(row):
        numbers = []
        for i,c in enumerate(row):
            if c.isnumeric():
                numbers.append(c)
            if c in alpha_map:
                for alpha in alpha_map[c]:
                    if alpha == row[i:i+len(alpha)]:
                        numbers.append(alpha_values[alpha])
        return int(numbers[0]+numbers[-1])

    print(sum(translate(row) for row in lines))

if __name__ == '__main__':
    day2()