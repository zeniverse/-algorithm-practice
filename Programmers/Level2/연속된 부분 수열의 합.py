

def solution(sequence, k):
    res = []
    sum = 0
    left = 0
    right = -1

    while True:
        if sum < k :
            right += 1
            if right >= len(sequence):
                break
            sum += sequence[right]
        else:
            sum -= sequence[left]
            if left >= len(sequence):
                break
            left += 1

        if sum == k:
            res.append([left, right])

    res.sort(key=lambda x:(x[1] - x[0], x[0]))
    return res[0]

sequence = [1, 2, 3, 4, 5]
k = 7
print(solution(sequence, k))

