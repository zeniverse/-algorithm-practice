
n = 3628800

def solution(n):
    num = 1

    for i in range(1, 11):
        num *= i

        if num > n:
            return i - 1
        elif num == n:
            return i
        


print(solution(n))
