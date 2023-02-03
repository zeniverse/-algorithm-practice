
def solution(n):
    res = 0

    for i in range(1, n + 1):
        s = 0

        while s < n:
            s += i
            i += 1
        
        if s == n:
            res += 1
        
    return res
        

n = 15
print(solution(n))