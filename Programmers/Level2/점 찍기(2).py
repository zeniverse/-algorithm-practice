
def solution(k, d):
    res = 0

    for y in range(0, d + 1, k):
        x = int((d ** 2 - y ** 2) ** 0.5)
        res += x // k + 1
        
    return res

k = 2
d = 4
print(solution(k, d))

