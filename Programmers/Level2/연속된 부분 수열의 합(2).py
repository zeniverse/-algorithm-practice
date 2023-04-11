

def solution(sequence, k):
    res = []
    arr = [sequence[0]]

    for i in range(1, len(sequence)):
        num = sequence[i] + arr[-1]
        arr.append(num)

    start, end = 0, 0
    ans = None
    ans_idx = None
    cnt = 0

    while start <= end and end < len(sequence):
        s = arr[start]
        e = arr[end]

        val = e - s + sequence[start]

        if val == k:
            if ans is None:
                res = [start, end]
            else:
                if res[-1] - res[0] > end - start:
                    res = [start, end]

        if start == end:
            end += 1
        elif val > k:
            start += 1
        else:
            end += 1

    return res

sequence = [1, 2, 3, 4, 5]
k = 7
print(solution(sequence, k))

