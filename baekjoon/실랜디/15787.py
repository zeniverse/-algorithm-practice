n, m = map(int, input().split())
train  = [[0 for _ in range(20)] for _ in range(n)]
res = []

for _ in range(m):
    arr = list(map(int, input().split()))

    if arr[0] == 1:
        train[arr[1] - 1][arr[2] - 1] = 1
    elif arr[0] == 2:
        train[arr[1] - 1][arr[2] - 1] = 0
    
    elif arr[0] == 3:
        for j in range(19, 0, -1):
            train[arr[1] - 1][j] = train[arr[1] - 1][j - 1]
        train[arr[1] - 1][0] = 0

    elif arr[0] == 4:
        for j in range(19):
            train[arr[1] - 1][j] = train[arr[1] - 1][j + 1]
        train[arr[1] - 1][19] = 0

for i in range(n):
    if train[i] not in res:
        res.append(train[i])

print(len(res))