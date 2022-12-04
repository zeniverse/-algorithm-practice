
i = 1
j = 13
k = 1

def solution(i, j, k):
    res = 0

    for num in range(i, j + 1):
        res += str(num).count(str(k))
        
    return res

print(solution(i, j, k))
