import heapq
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = []

for _ in range(n):
    tmp = list(map(int, input().split()))

    if arr:
        for n in tmp:
            if arr[0] < n:
                heapq.heappop(arr)
                heapq.heappush(arr, n)
    else:
        for n in tmp:
            heapq.heappush(arr, n)

print(arr[0])
