import heapq

def solution(operations):
    queue = []

    for i in operations:
        s, n = i.split(" ")
        if s == "I":
            heapq.heappush(queue, int(n))
        elif s == "D" and queue:
            if n == "1":
                queue = heapq.nlargest(len(queue), queue)[1:]
                heapq.heapify(queue)
            else:
                heapq.heappop(queue)

    if queue:
        return [max(queue), min(queue)]
    return [0, 0]

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))