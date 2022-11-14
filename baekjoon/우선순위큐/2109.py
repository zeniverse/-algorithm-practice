import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    p, d = map(int, input().split())
    arr.append((d, p))

arr.sort()
heap = []

for i in range(n):
    heapq.heappush(heap, arr[i][1])

    if len(heap) > arr[i][0]:
        heapq.heappop(heap)

print(sum(heap))