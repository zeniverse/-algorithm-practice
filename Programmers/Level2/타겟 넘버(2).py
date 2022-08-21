from itertools import product


numbers = [1, 1, 1, 1, 1]
target = 3

arr = [(i, -i) for i in numbers]
s = list(map(sum, product(*arr)))

print(s.count(target))