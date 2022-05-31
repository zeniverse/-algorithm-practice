from itertools import combinations
import sys
input = sys.stdin.readline

def gcd(a, b):
    if b > a:
        a, b = b, a

    if b == 0:
        return a
    return gcd(b, a % b)

for _ in range(int(input())):
    n, *arr = map(int, input().split())
    sum = 0

    combi = combinations(arr, 2)

    for a, b in combi:
        sum += gcd(a, b)

    print(sum)
