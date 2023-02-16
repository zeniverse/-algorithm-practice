import heapq

def solution(n, works):

    if sum(works) <= n:
        return 0
    
    works = [-w for w in works]
    heapq.heapify(works)

    for _ in range(n):
        num = heapq.heappop(works)
        num += 1
        heapq.heappush(works, num)

    return sum([i ** 2 for i in works])
    

n, works = 4, [4, 3, 3]
print(solution(n, works))

