from collections import defaultdict
import sys, heapq

input = sys.stdin.readline

n = int(input())
minH, maxH = [], []
visited = defaultdict(bool)

for _ in range(n):
    number, level = map(int, input().split())

    heapq.heappush(minH, (level, number))
    heapq.heappush(maxH, (-level, -number))
    visited[number] = True

for _ in range(int(input())):
    command = input().strip().split()

    if command[0] == 'add':
        number, level = int(command[1]), int(command[2])

        while not visited[minH[0][1]]:
            heapq.heappop(minH)
        while not visited[-maxH[0][1]]:
            heapq.heappop(maxH)

        heapq.heappush(minH, (level, number))
        heapq.heappush(maxH, (-level, -number))
        visited[number] = True
    
    elif command[0] == 'solved':
        visited[int(command[1])] = False

    elif command[1] == '1':
        while not visited[-maxH[0][1]]:
            heapq.heappop(maxH)

        print(-maxH[0][1])
    else:
        while not visited[minH[0][1]]:
            heapq.heappop(minH)
            
        print(minH[0][1])
        

