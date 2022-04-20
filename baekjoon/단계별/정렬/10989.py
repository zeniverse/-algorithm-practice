import sys
input = sys.stdin.readline

n = int(input())
count = [0] * 10001

for i in range(n):
    data = int(input())
    count[data] += 1

for i in range(10001):
    if count[i] != 0:
        for j in range(count[i]):
            print(i)