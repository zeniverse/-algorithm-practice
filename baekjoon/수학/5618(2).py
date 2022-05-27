import sys
input = sys.stdin.readline

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

n = int(input())
arr = list(map(int, input().split()))
g_num = gcd(arr[0], gcd(arr[1], arr[-1]))

for i in range(1, (g_num//2) + 1):
    if g_num % i == 0:
        print(i)
print(g_num)
