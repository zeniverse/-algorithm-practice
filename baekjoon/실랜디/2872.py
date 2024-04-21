import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

target = n
res = 0

for i in range(n - 1, -1, -1):
    if arr[i] != target:
        res += 1
    else:
        target -= 1

print(res)
