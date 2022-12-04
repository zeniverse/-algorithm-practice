from math import factorial

n = 3628800

def solution(n):
    k = 10

    while n < factorial(k):
        k -= 1
    
    return k
    

print(solution(n))
