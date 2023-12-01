f = open("input.txt", "r")
lines = f.readlines()
print(sum(int([c for c in row if c.isnumeric()][0] + [c for c in row if c.isnumeric()][-1]) for row in lines))