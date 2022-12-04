
n = 10

def solution(n):
    res = 0

    for i in range(4, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                res += 1
                break
                
    return res

print(solution(n))
