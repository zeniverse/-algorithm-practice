from itertools import combinations
import sys

s = sys.stdin.readline().strip()
arr = []
stack = []
res = set()

for idx, v in enumerate(list(s)):
    if v == '(':
        stack.append(idx)
    elif v == ')':
        start = stack.pop()
        end = idx
        arr.append([start, end])


for i in range(1, len(arr) + 1):
    combi = combinations(arr, i)

    for j in combi:
        tmp = list(s)
        for k in j:
            start, end = k
            tmp[start] = ''
            tmp[end] = ''
        res.add(''.join(tmp))

for i in sorted(list(res)):
    print(i)


