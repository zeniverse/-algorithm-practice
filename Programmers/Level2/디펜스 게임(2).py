import heapq

n, k, enemy = 7, 3, [4, 2, 4, 5, 3, 3, 1]

def solution(n, k, enemy):
    queue = enemy[:k]
    heapq.heapify(queue)

    for idx in range(k, len(enemy)):
        n -= heapq.heappushpop(queue, enemy[idx])

        if n < 0:
            return idx
    return len(enemy)

print(solution(n, k, enemy))