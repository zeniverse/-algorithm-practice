
score = [[1, 2], [1, 1], [1, 1]]

def solution(score):
    res = []
    
    for i in range(len(score)):
        if sum(score[i]) == 0:
            score[i] = 0
        else:
            score[i] = sum(score[i]) / 2

    arr = sorted(score, reverse=True)

    for i in range(len(score)):
        res.append(arr.index(score[i]) + 1)

    return res 

print(solution(score))


# [[1, 2], [1, 1], [1, 1]] -> [1, 2, 2]