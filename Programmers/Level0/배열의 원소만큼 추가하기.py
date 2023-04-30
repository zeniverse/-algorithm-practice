
def solution(arr):
    res = []
    for i in arr:
        for _ in range(int(i)):
            res.append(i)
    return res

arr = [5, 1, 4]
print(solution(arr))