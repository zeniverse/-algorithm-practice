n = 3
numlist = [4, 5, 6, 7, 8, 9, 10, 11, 12]

def solution(n, numlist):
    res = []

    for i in numlist:
        if not i % n:
            res.append(i)

    return res

print(solution(n, numlist))
