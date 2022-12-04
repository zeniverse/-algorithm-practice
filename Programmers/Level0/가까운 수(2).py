import sys

array = [10, 11, 12]
n = 13

def solution(array, n):
    array.sort(key=lambda x:(abs(x - n), x - n))

    return array[0]


print(solution(array, n))
