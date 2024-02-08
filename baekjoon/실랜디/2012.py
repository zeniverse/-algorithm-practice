import sys
input = sys.stdin.readline

n = int(input())
arr = []
res = 0

for _ in range(n):
    arr.append(int(input()))

arr.sort()

for i in range(1, n + 1):
    res += abs(i - arr[i - 1])

print(res)