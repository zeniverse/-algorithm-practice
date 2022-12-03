box = [10, 8, 6]
n = 3

def solution(box, n):
    res = 1

    for i in box:
        res *= i // n

    return res


print(solution(box, n))
