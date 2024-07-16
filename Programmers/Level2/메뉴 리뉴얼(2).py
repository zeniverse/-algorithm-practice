
from collections import Counter
from itertools import combinations


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

def solutions(orders, course):
    answer = []

    for c in course:
        order_combi = []

        for order in orders:
            order_combi += combinations(sorted(order), c)

        most_ordered = Counter(order_combi).most_common()
        answer += [k for k, v in most_ordered if v > 1 and v == most_ordered[0][1]]

    return [''.join(v) for v in sorted(answer)]

print(solutions(orders, course))
    