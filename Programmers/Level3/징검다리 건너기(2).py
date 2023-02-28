
import heapq, sys

def solution(stones, k):
    n = len(stones)

    queue = []
    res = sys.maxsize

    for i in range(k - 1):
        heapq.heappush(queue, [-stones[i], i])
    
    for i in range(k - 1, n):
        heapq.heappush(queue, [-stones[i] ,i])
        print(queue)
        while queue[0][1] < i - k + 1:
            heapq.heappop(queue)

        res = min(res, -queue[0][0])
    

    return res

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))