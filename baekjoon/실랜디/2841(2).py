import sys
input = sys.stdin.readline

n, p = map(int, input().split())
arr = [[0] for _ in range(7)]
res = 0

for _ in range(n):
    line, num = map(int, input().split())

    while arr[line][-1] > num:
        arr[line].pop()
        res += 1

    if arr[line][-1] == num:
        continue

    arr[line].append(num)
    res += 1

print(res)