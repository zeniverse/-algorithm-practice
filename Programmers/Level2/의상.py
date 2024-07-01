from collections import defaultdict

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution(clothes):
    answer = 1
    dic = defaultdict(list)

    for i in clothes:
        dic[i[1]].append(i[0])
    
    for k, v in dic:
        answer *= (len(v) + 1)

    return answer

print(solution(clothes))