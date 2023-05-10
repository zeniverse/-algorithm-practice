
def solution(arr, queries):
    res = []

    for s, e, k in queries:
        num = 1000001
        for i in range(s, e + 1):
            if arr[i] > k:
                num = min(num, arr[i])
        if num == 1000001:
            res.append(-1)
        else:
            res.append(num)

    return res


arr = [0, 1, 2, 4, 3]
queries = [[0, 4, 2],[0, 3, 2],[0, 2, 2]]
print(solution(arr, queries))