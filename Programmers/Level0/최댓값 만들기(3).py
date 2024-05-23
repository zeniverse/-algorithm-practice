from itertools import combinations
import sys

numbers = [1, 2, -3, 4, -5]

def solution(numbers):
    numbers.sort()
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])


print(solution(numbers))
