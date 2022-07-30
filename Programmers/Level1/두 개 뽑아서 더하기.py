import itertools

numbers = [2,1,3,4,1]
res = set()

for a, b in itertools.combinations(numbers, 2):
    res.add(a + b)

res = list(res)
res.sort()

print(res)

