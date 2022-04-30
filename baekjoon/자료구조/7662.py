import sys, heapq

n = int(sys.stdin.readline())
res = []

for _ in range(n):
    visited = [False] * 1000001
    minH, maxH = [], []

    for i in range(int(sys.stdin.readline())):
        order = sys.stdin.readline().strip().split()

        if order[0] == 'I':
            heapq.heappush(minH, (int(order[1]), i))
            heapq.heappush(maxH, (-int(order[1]), i))
            visited[i] = True

        elif order[1] == '1':
            while maxH and not visited[maxH[0][1]]:
                heapq.heappop(maxH)
            
            if maxH:
                visited[maxH[0][1]] = False
                heapq.heappop(maxH)
        
        else:
            while minH and not visited[minH[0][1]]:
                heapq.heappop(minH)
            
            if minH:
                visited[minH[0][1]] = False
                heapq.heappop(minH)

    while minH and not visited[minH[0][1]]:
        heapq.heappop(minH)
    while maxH and not visited[maxH[0][1]]:
        heapq.heappop(maxH)

    res.append(f'{-maxH[0][0]} {minH[0][0]}' if minH and maxH else "EMPTY")

print('\n'.join(res))

