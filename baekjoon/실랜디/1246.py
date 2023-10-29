import sys

input = sys.stdin.readline

n, m = map(int, input().split())
ps = [int(input()) for _ in range(m)]
ps.sort(reverse=True)

price = -1
profit = -1
loop = m if n > m else n
for i in range(loop):
    temp = ps[i] * (i + 1)

    if profit <= temp:
        profit = temp
        price = ps[i]

print(price, profit)