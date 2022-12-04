
n = 10

def solution(n):
    res = 0

    for i in range(1, n  + 1):
        arr = set()
        for j in range(1, i + 1):
            if i % j == 0:
                arr.add(j)

        if len(arr) >= 3:
            res += 1
                
    return res

print(solution(n))
