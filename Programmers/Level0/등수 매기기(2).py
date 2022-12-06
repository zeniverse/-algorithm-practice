
score = [[1, 2], [1, 1], [1, 1]]

def solution(score):
    arr = sorted([sum(i) for i in score], reverse=True)
    return [arr.index(sum(i)) + 1 for i in score] 

print(solution(score))


# [[1, 2], [1, 1], [1, 1]] -> [1, 2, 2]