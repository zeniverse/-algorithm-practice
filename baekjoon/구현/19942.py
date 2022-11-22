from itertools import combinations
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
mp, mf, ms, mv = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
res = INF

combi = []
ans = []

for i in range(1, n + 1):
    combi.extend(combinations([i for i in range(1, n + 1)], i))

for com in combi:
    p_sum, f_sum, s_sum, v_sum = 0, 0, 0, 0
    total = 0
    for i in com:
        p_sum += arr[i - 1][0]
        f_sum += arr[i - 1][1]
        s_sum += arr[i - 1][2]
        v_sum += arr[i - 1][3]

        total += arr[i - 1][4]

    if p_sum >= mp and f_sum >= mf and s_sum >= ms and v_sum >= mv:
        if res > total:
            res = total
            ans = com
        elif res == total:
            ans = sorted((ans, com))[0]

if res == INF:
    print(-1)
else:
    print(res)
    print(*ans)