import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

for _ in range(int(input())):
    a, b = map(int, input().split())

    if b > a:
        a, b = b, a

    g = gcd(a, b)
    print((a * b)//g)


