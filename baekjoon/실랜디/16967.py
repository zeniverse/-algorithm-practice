import sys
input = sys.stdin.readline

h, w, x, y = map(int, input().split())
arr_b = [list(map(int, input().split())) for _ in range(h + x)]
res = []

for i in range(h):
    res.append(arr_b[i][:w])

for i in range(x, h):
    for j in range(y, w):
        res[i][j] = arr_b[i][j] - res[i - x][j - y]

for i in res:
    print(" ".join(map(str, i)))