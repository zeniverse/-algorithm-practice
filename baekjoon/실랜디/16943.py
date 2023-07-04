from itertools import permutations

a, b = input().split()
b = int(b)
arr = list(map(lambda x: ''.join(x), permutations(a)))
res = -1

for i in arr:
    if int(i) <= b and i[0] != '0':
        res = max(res, int(i))

print(res)


