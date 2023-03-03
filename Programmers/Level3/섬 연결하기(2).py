

def find_parent(parent, x):
    if parent[x] == x:
        return x
    else:
        return find_parent(parent, parent[x])

def solution(n, costs):
    res = 0
    costs = sorted([(x[2], x[0], x[1]) for x in costs])
    parent = [i for i in range(n)]
    bridges = 0

    for a, b, c in costs:
        if find_parent(parent, b) != find_parent(parent, c):
            res += a
            parent[find_parent(parent, b)] = c
            bridges += 1

        if bridges == n - 1:
            break

    return res

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs))