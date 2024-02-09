import sys

t = int(sys.stdin.readline())

for _ in range(t):
    sys.stdin.readline()
    arr = []
    count = 0
    r, c = map(int, sys.stdin.readline().split())
    for _ in range(r):
        arr.append(sys.stdin.readline())
    for i in range(r):
        for j in range(c-2):
            if arr[i][j] == '>' and arr[i][j+1] == 'o' and arr[i][j+2] == '<':
                count += 1
    for i in range(r-2):
        for j in range(c):
            if arr[i][j] == 'v' and arr[i+1][j] == 'o' and arr[i+2][j] == '^':
                count += 1
    print(count)