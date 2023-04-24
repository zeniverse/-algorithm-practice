def solution(arr, k):
    if k % 2 == 0:
        return [i + k for i in arr]
    return [i * k for i in arr]

arr = [1, 2, 3, 100, 99, 98]
k = 3
print(solution(arr, k))