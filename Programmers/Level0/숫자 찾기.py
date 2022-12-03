
num = 29183
k = 1

def solution(num, k):
    res = str(num).find(str(k))

    if res != -1:
        return res + 1
    return res

print(solution(num, k))
