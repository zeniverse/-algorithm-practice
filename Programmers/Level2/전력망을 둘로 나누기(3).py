n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]

parent = []

def find(a):
    global parent

    if parent[a] < 0:
        return a

    parent[a] = find(parent[a])
    return parent[a]


    
def union(a, b):
    global parent

    parent_a = find(a)
    parent_b = find(b)

    if parent_a == parent_b:
        return

    parent[parent_a] += parent[parent_b]
    parent[parent_b] = parent_a


def solution(n, wires):
    global parent
    res = int(1e9)
    
    for i in range(len(wires)):
        parent = [-1] * (n + 1)
        tmp = [wires[k] for k in range(len(wires)) if k != i]

        for v1, v2 in tmp:
            union(v1, v2)

        v = [x for x in parent[1:] if x < 0]
        res = min(res, abs(v[0] - v[1]))

    return res

print(solution(n, wires))