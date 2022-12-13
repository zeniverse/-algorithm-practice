
k, score = 4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]

def solution(k, score):
    res = []
    top = []

    for s in score:
        if len(top) < k:
            top.append(s)
        else:
            if s > min(top):
                top.pop(0)
                top.append(s)
        top.sort()
        res.append(min(top))

    return res
    

print(solution(k, score))