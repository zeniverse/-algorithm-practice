
def solution(n):
    res = 1

    while n > 1:
        res += n % 2
        n //= 2
    
    return res


n = 5000
print(solution(n))
