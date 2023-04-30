
def solution(arr):
    res = []
    for i in arr:
        res += [i] * int(i)
    return res

arr = [5, 1, 4]
print(solution(arr))