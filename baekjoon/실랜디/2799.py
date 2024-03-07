m, n = map(int, input().split())
arr = [input() for _ in range((5 * m) + 1)]
apt = ['................', '****............', '********........', '************....', '****************']

row, col = [], []

for i in range(m):
    row.append(5 * i + 1)

for i in range(n):
    col.append(5 * i + 1)

cnt = []

for i in row:
    for j in col:
        tmp = ''
        tmp += arr[i][j:j + 4]
        tmp += arr[i + 1][j:j + 4]
        tmp += arr[i + 2][j:j + 4]
        tmp += arr[i + 3][j:j + 4]
        cnt.append(tmp)

res = [0] * 5

for i in range(5):
    res[i] = cnt.count(apt[i])

print(*res)