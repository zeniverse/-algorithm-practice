import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    arr = list(map(int, input().split()))
    res = 0
    
    heapq.heapify(arr)

    while len(arr) > 1:
        c1 = heapq.heappop(arr)
        c2 = heapq.heappop(arr)

        res += (c1 + c2)
        heapq.heappush(arr, c1 + c2)

    print(res)


