
numbers = [1, 2, 3, 4]
k = 2

def solution(numbers, k):
    count = 2 * (k - 1)
    return numbers[count % len(numbers)]


print(solution(numbers, k))
