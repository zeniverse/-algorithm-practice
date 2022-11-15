import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
rotate = [[0] * n for _ in range(m)]

s = [45, 124, 47, 92, 94, 60, 118, 62]
s_rotate = [124, 45, 92, 47, 60, 118, 62, 94]

for j in range(n):
    for i in range(m):
        if ord(arr[j][i]) in s:
            rotate[m-1-i][j] = chr(s_rotate[s.index(ord(arr[j][i]))])
        else:
            rotate[m-1-i][j] = arr[j][i]
        # print(m -1-i, j)
        # rotate[m-1-i][j] = arr[j][i]

for i in rotate:
    print(''.join(i))
