n, m = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(n)]

m, k = map(int, input().split())
arr2 = [list(map(int, input().split())) for _ in range(m)]

res = [[0] * k for _ in range(n)]

for row in range(n):
    for col in range(k):
        tmp = 0
        for i in range(m):
            tmp += arr1[row][i] * arr2[i][col]
        res[row][col] = tmp

for i in res:
    print(*i)