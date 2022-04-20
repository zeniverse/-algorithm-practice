import sys

n = int(sys.stdin.readline())
arr = sorted([int(input()) for _ in range(n)])

for i in arr:
    print(i)