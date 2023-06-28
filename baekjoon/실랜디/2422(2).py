from collections import defaultdict
from itertools import combinations

n, m = map(int, input().split())
arr = [[False] * n for _ in range(n)]
dic = defaultdict(set)

for _ in range(m):
    a, b = map(int, input().split())
    dic[a].add(b)
    dic[b].add(a)

res = 0

for combi in combinations(range(1, n + 1), 3):
    if combi[1] not in dic[combi[0]] and combi[2] not in dic[combi[0]] and combi[1] not in dic[combi[2]]:
        res += 1

print(res)





