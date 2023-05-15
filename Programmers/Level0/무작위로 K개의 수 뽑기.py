
def solution(arr, k):
    res = []
    for i in arr:
        if i not in res:
            res.append(i)
        if len(res) == k:
            return res
    return res + ([-1] * (k - len(res)))
        
arr = [0, 1, 1, 1, 1]
k = 4
print(solution(arr, k))