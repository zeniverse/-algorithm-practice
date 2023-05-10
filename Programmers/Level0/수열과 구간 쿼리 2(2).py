
def solution(arr, queries):
    res = []

    for s, e, k in queries:
        tmp = []
        for i in arr[s:e + 1]:
            if i > k:
                tmp.append(i)
        res.append(-1 if not tmp else min(tmp))

    return res


arr = [0, 1, 2, 4, 3]
queries = [[0, 4, 2],[0, 3, 2],[0, 2, 2]]
print(solution(arr, queries))