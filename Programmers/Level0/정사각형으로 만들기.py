
def solution(arr):
    n = len(arr)
    m = len(arr[0])

    if n > m:
        for i in arr:
            i += [0] * (n - m)
    elif m > n:
        for _ in range(m - n):
            arr.append([0] * m)

    return arr


arr = [[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]]
print(solution(arr))