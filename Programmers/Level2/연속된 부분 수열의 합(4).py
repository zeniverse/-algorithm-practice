

def solution(sequence, k):
    answer = []
    length = len(sequence)
    
    arr = [0]

    for i in sequence:
        arr.append(arr[-1] + i)

    start, end = 0, 1
    tmp = 1000001

    while start <= end <= length:
        current = arr[end] - arr[start]

        if current == k:
            if tmp > end - start:
                answer = [start, end - 1]
                tmp = end - start
            end += 1
        elif current < k:
            end += 1
        elif current > k:
            start += 1

    return answer

sequence = [1, 2, 3, 4, 5]
k = 7
print(solution(sequence, k))

