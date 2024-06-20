
n = 10

def prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def solution(n):
    answer = 0
    for i in range(2, n + 1):
        if prime(i):
            answer += 1
    return answer

print(solution(n))

