import heapq

n, k, enemy = 7, 3, [4, 2, 4, 5, 3, 3, 1]

def solution(n, k, enemy):
    res = 0
    heap = []
    enemySum = 0

    for e in enemy:
        heapq.heappush(heap, -e)
        enemySum += e

        if enemySum > n:
            if k == 0: break
            enemySum += heapq.heappop(heap)
            k -= 1
        res += 1
    return res

print(solution(n, k, enemy))