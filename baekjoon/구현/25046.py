from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
combi = list()

for i in range(1, n + 1):
    for x in combinations([i for i in range(n)], i):
        combi.append(x)

res = -sys.maxsize

# 모든 열의 합
s = list() 

for i in range(n):
    tmp = 0
    for j in range(n):
        tmp += arr[j][i]
    s.append(tmp)

for rows in combi:
    ans_tmp = 0
    for i in range(n):
        tmp = 0
        for r in rows:
            tmp += arr[r][i]

        # 모든 열의 합 - 민우가 선택한 열의 합(tmp) 과 민우가 선택한 열의 합을 비교해 작은값을 선택
        # 민우가 이기려고 하듯, 종진이도 이기려고 하기 때문에
        # 여기서 민우는 s[i] - tmp, tmp중 큰 값을 선택할 것이다.
        # 따라서 민우가 얻을 수 있는 점수는 min값이어야한다.
        ans_tmp += min(s[i] - tmp, tmp)
    
    res = max(ans_tmp, res)

print(res)