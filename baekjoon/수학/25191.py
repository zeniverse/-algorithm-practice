import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split(" "))

cnt = 0
cnt += a // 2
cnt += b

print(min(n, cnt))