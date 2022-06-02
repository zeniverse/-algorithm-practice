import sys, math
input = sys.stdin.readline

n = int(input())
a = set(list(map(int, input().split())))

isPrime = [False, False] + [True] * (1_000_000 - 1)

for i in range(2, int(math.sqrt(1000000)) + 1):
    if isPrime[i]:
        for j in range(i * i, 1000000, i):
            isPrime[j] = False

res = 1

for i in a:
    if isPrime[i]:
        res *= i

if res == 1:
    print(-1)
else:
    print(res)