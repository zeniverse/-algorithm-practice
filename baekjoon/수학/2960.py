import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [True] * (n + 1)
count = 0

for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if arr[j] == True:
            arr[j] = False
            count += 1

            if count == k:
                print(j)
                break


