import heapq

def solution(operations):
    heap = []
    max_heap = []

    for i in operations:
        s, n = i.split(" ")
        if s == "I":
            heapq.heappush(heap, int(n))
            heapq.heappush(max_heap, (-int(n), int(n)))
        elif s == "D" and heap:
            if n == "1":
                value = heapq.heappop(max_heap)[1]
                heap.remove(value)
                heapq.heapify(heap)
            else:
                heapq.heappop(heap)

    if heap:
        return [heapq.heappop(max_heap)[1], heapq.heappop(heap)]
    return [0, 0]

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))