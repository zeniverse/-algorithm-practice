import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

flag = 0 
count = 0

for i in range(n):
    flag = arr[flag]
    count += 1

    if flag == k:
        print(count)
        exit(0)

print(-1)