

def solution(numbers, n):
    res = 0

    for num in numbers:
        if res <= n:
            res += num
        else:
            return res
    return res

numbers = [58, 44, 27, 10, 100]
n = 139
print(solution(numbers, n))
