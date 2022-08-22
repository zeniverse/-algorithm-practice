
from collections import Counter
from itertools import combinations


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

res = []

for c in course:
    tmp = []
    for order in orders:
        combi = combinations(sorted(order), c)
        tmp += combi
    
    print(Counter(tmp))
    counter = Counter(tmp)

    if len(counter) != 0 and max(counter.values()) != 1:
        res += [''.join(i) for i in counter if counter[i] == max(counter.values())]

print(sorted(res))
    