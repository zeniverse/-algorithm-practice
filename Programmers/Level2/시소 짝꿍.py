from collections import Counter

def solution(weights):
    res = 0

    count = Counter(weights)

    # 중복되는 경우 갯수 계산
    # 4C2는 4 * (4 - 1) / 2 => 계산법 이용
    for k, v in count.items():
        if v > 1:
            res += v * (v - 1) // 2
    
    # 중복되지 않는 경우 계산하기 위해 중복값 없애주기
    weights = list(set(weights))
    check = (3/4, 2/3, 1/2)

    for w in weights:
        for c in check:
            if w * c in weights:
                print(w * c, w, c)
                res += count[w] * count[w * c]

    return res

weights = [100,180,360,100,270]

print(solution(weights))