n, m = map(int, input().split())

arr = [0] * m
isused = [False] * (n + 1)

def find(k):
    if k == m:
        print(*arr)
        return

    for i in range(1, n + 1):
        if not isused[i]:
            arr[k] = i
            isused[i] = True
            find(k + 1)
            isused[i] = False

find(0)