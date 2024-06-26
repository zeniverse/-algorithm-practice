
n = 3

def solution(n):
    if n ** 0.5 == int(n ** 0.5):
        return (n ** 0.5 + 1) ** 2
    return -1


print(solution(n))