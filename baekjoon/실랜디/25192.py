import sys
input = sys.stdin.readline

n = int(input())
arr = set()
res = 0

for _ in range(n):
    s = input().strip()

    if s == 'ENTER':
        res += len(arr)
        arr = set()
    else:
        arr.add(s)

res += len(arr)

print(res)