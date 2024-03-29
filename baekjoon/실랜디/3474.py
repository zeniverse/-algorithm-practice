import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    res = 0

    i = 5
    while i <= n:
        res += n // i
        i *= 5
    
    print(res)