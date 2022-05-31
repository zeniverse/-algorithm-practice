import sys
input = sys.stdin.readline

def gcd(a, b):
    if b > a:
        a, b = b, a

    if b == 0:
        return a
    return gcd(b, a % b)

n = int(input())
a = list(map(int, input().split()))
x = int(input())
res = []

for i in a:
    if gcd(i, x) == 1:
        res.append(i)

print('%0.6f' %(sum(res)/len(res)))

