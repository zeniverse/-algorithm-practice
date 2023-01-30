import heapq

def solution(numbers):
    res = [-1] * len(numbers)

    heap = []

    for i in range(len(numbers)):
        value = numbers[i]

        while heap and heap[0][0] < value:
            x, idx = heapq.heappop(heap)
            res[idx] = value

        heapq.heappush(heap, [value, i])

    return res

numbers = [9, 1, 5, 3, 6, 2]
print(solution(numbers))