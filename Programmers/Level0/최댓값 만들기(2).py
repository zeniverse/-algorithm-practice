from itertools import combinations
import sys

numbers = [1, 2, -3, 4, -5]

def solution(numbers):
    res = -sys.maxsize

    for a, b in combinations(numbers, 2):
        if a * b > res:
            res = a * b
        
    return res


print(solution(numbers))
