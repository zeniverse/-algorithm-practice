from collections import Counter

def solution(weights):
    res = 0

    count = Counter(weights)
    weights_key = list(count.keys())

    for idx1 in range(len(weights_key)):
        for idx2 in range(idx1, len(weights_key)):
            w1, w2 = weights_key[idx1], weights_key[idx2]

            if idx1 == idx2 and 1 < count[w1]:
                res += count[w1] * (count[w1] - 1) // 2
                continue

            if w1*2 == w2*3:
                res += count[w1] * count[w2]
            if w1*2 == w2*4:
                res += count[w1] * count[w2]
            if w1*3 == w2*2:
                res += count[w1] * count[w2]
            if w1*3 == w2*4:
                res += count[w1] * count[w2]
            if w1*4 == w2*2:
                res += count[w1] * count[w2]
            if w1*4 == w2*3:
                res += count[w1] * count[w2]

    return res

weights = [100,180,360,100,270]

print(solution(weights))