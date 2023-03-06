import heapq

def solution(jobs):
    res, now, idx = 0, 0, 0
    start = -1
    heap = []

    while idx < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])
                print(heap)
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            res += (now - current[1])
            idx += 1
        else:
            now += 1

    return int(res / len(jobs))

jobs =[[0, 3], [1, 9], [2, 6]]
print(solution(jobs))