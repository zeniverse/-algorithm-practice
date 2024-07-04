

def solution(sequence, k):
    answer = []

    start, end = 0, 0
    tmp = sequence[0]
    min_len = 1000001

    while start <= end < len(sequence):
        if tmp == k:
            if end - start + 1 < min_len:
                min_len = end - start + 1
                answer = [start, end]
            tmp -= sequence[start]
            start += 1
        elif tmp < k:
            end += 1
            if end < len(sequence):
                tmp += sequence[end]
        elif tmp > k:
            tmp -= sequence[start]
            start += 1

    return answer

sequence = [1, 2, 3, 4, 5]
k = 7
print(solution(sequence, k))

