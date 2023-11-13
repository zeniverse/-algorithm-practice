import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dict = {}

for n in range(N):
    key, value = input().split()
    dict[key] = value

for m in range(M):
    key = input().strip()
    print(dict[key])