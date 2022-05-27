import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
limit = min(arr) + 1
res = []

for i in range(1, limit):
    count = 0
    for num in arr:
        if num % i == 0:
            count += 1

    if count == len(arr):
        print(i)
