from itertools import combinations_with_replacement

n = int(input())
rome = [1, 5, 10, 50]


comb = list(combinations_with_replacement(rome, n))
data = set([])
for t in comb:
    data.add(sum(t))

print(len(data))