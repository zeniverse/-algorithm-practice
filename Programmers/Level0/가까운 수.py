import sys

array = [10, 11, 12]
n = 13

def solution(array, n):
    diff = sys.maxsize
    res = 0
    array.sort()

    for i in array:
        if diff > abs(n - i):
            diff = abs(n - i)
            res = i

    return res


print(solution(array, n))
