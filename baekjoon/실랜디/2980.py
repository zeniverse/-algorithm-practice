import sys
input = sys.stdin.readline

n, l = map(int, input().split())
current = 0
res = 0

for _ in range(n):
    d, r, g = map(int, input().split())

    res += (d - current)
    current = d

    if res % (r + g) <= r:
        res += (r - (res % r + g))

res += (l - current)
print(res)