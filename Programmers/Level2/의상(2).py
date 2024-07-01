from collections import Counter
from functools import reduce

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution(clothes):
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x + y + (x * y), cnt.values())

    return answer

print(solution(clothes))