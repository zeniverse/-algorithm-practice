from collections import defaultdict

def solution(weights):
    answer = 0

    dic = defaultdict(float)
    ratio = [1/1, 2/4, 2/3, 3/2, 3/4, 4/2, 4/3]

    for w in weights:
        for r in ratio:
            answer += dic[w * r]
        dic[w] += 1
    
    return int(answer)

weights = [100,180,360,100,270]

print(solution(weights))