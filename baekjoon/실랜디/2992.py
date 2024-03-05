from itertools import permutations

x = list(input())
res = []

for per in permutations(x, len(x)):
    if int(''.join(x)) < int(''.join(per)):
        res.append(int(''.join(per)))

res.sort()
if res:
    print(res[0])
else:
    print(0)