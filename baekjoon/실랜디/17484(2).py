

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
directions = {1: (1, -1), 2: (1, 0), 3:(1, 1)}

def dfs(i, j, now_dir, min_fuel, fuel):
    if i == n - 1:
        return min(min_fuel, fuel)
    
    for k in range(1, 4):
        if now_dir != k:
            if 0 <= i + directions[k][0] < n and 0 <= j + directions[k][1] < m :
                min_fuel = dfs(i + directions[k][0], j + directions[k][1], k, min_fuel, fuel + arr[i + directions[k][0]][j + directions[k][1]])

    return min_fuel

min_fuel = int(1e9)

for i in range(m):
    min_fuel = min(dfs(0, i, 0, min_fuel, arr[0][i]), min_fuel)

print(min_fuel)