from itertools import permutations

numbers = [1, 2, 3, 4, 5]

def solution(numbers):
    res = 0

    for a, b in permutations(numbers, 2):
        res = max(res, a * b)
    
    return res

print(solution(numbers))