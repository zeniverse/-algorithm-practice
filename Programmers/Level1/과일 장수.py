k, m, score = 3, 4, [1, 2, 3, 1, 2, 3, 1]

def solution(k, m, score):
    res = 0
    score = sorted(score, reverse=True)

    for i in range(0, len(score), m):
        tmp = score[i:i + m]

        if len(tmp) == m:
            res += min(tmp) * m

    return res

print(solution(k, m, score))