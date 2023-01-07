from collections import Counter

tangerine = [1, 1, 1, 1, 2, 2, 2, 3]
k = 2

def solution(k, tangerine):
    res = 0
    total = 0

    for key, v in Counter(tangerine).most_common():
        total += v
        res += 1

        if total >= k:
            return res

print(solution(k, tangerine))
