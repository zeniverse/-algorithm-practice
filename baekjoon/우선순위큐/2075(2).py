import heapq
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = []

for _ in range(n):
    for num in map(int, input().split()):
        heapq.heappush(arr, num)

    #heapq.nlargest, nsmallest 기억하기!
    arr = heapq.nlargest(n, arr)

print(arr[-1])
