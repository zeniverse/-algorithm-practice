k, m, score = 3, 4, [1, 2, 3, 1, 2, 3, 1]

def solution(k, m, score):
    res = 0
    
    # print(sorted(score))
    # print(len(score) % m)
    # print(sorted(score)[len(score) % m::m])

    return sum(sorted(score)[len(score) % m::m]) * m

print(solution(k, m, score))