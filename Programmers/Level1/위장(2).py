from functools import reduce
from collections import Counter


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]


cnt = Counter([kind for name, kind in clothes])
answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1

print(answer)