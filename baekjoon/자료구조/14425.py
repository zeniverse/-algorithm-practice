import sys

n, m = map(int, sys.stdin.readline().split())
s = []
res = 0

for i in range(n):
    data = sys.stdin.readline().strip()
    s.append(data)

for j in range(m):
    data = sys.stdin.readline().strip()
    
    if data in s:
        res += 1

print(res)
