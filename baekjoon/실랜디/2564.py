n, m = map(int, input().split())
store = int(input())
arr = []

def get_distance(dir, dist):
    if dir == 1:
        return dist
    elif dir == 2:
        return n + m + (n - dist)
    elif dir == 3:
        return n + m + n + (m - dist)
    else:
        return n + dist

for _ in range(store):
    direction, position = map(int, input().split())
    arr.append((direction, position))

start_d, start_p = map(int, input().split())

res = 0
dist1 = get_distance(start_d, start_p)

for d, p in arr:
    dist2 = get_distance(d, p)
    path1 = abs(dist1 - dist2)
    path2 = (2 * n + 2 * m) - path1

    res += min(path1, path2)

print(res)

