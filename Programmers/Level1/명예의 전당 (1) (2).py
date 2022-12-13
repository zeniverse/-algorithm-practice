import heapq

k, score = 4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]

def solution(k, score):
    res = []
    top = []

    for s in score:
        heapq.heappush(top, s)

        if len(top) > k:
            heapq.heappop(top)

        res.append(top[0])

    return res
    

print(solution(k, score))