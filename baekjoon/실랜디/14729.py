import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(float(input()))

arr.sort()

for i in arr[:7]:
    print("{:.3f}".format(i))