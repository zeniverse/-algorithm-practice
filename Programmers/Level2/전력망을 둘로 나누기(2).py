from collections import Counter
import sys

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(parent, a, b):
    a = find(a, parent)
    b = find(b, parent)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, wires):
    res = sys.maxsize

    for i in range(len(wires)):
        parent = [i for i in range(n + 1)]
        tmp = [wires[x] for x in range(len(wires)) if x != i]

        for a, b in tmp:
            if find(a, parent) == find(b, parent):
                continue
            union(parent, a, b)

        uf = []
        for i in range(1, n + 1):
            uf.append(find(i, parent))

        uf = Counter(uf).most_common()
        res = min(res, abs(uf[0][1] - uf[1][1]))

    return res

print(solution(n, wires))