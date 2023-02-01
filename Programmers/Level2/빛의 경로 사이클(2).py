#     ↓  ←   ↑  →
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def solution(grid):
    global visited, n, m
    res = []

    n = len(grid)
    m = len(grid[0])

    visited = [[[False] * 4 for _ in range(m)] for _ in range(n)]

    for start_x in range(n):
        for start_y in range(m):
            for d in range(4):
                if not visited[start_x][start_y][d]:
                    ans = simulate(start_x, start_y, d, grid)
                    if ans != 0:
                        res.append(ans)

    return sorted(res)


def simulate(sx, sy, sd, grid):
    global visited, n, m

    x, y, d = sx, sy, sd
    count = 0
    visited[x][y][d] = True

    while True:
        x = (x + dx[d]) % n
        y = (y + dy[d]) % m

        count += 1

        if grid[x][y] == 'L':
            d = (d - 1) % 4
        elif grid[x][y] == 'R':
            d = (d + 1) % 4

        if visited[x][y][d]:
            if (x, y, d) == (sx, sy, sd):
                return count
            else:
                return 0
            
        visited[x][y][d] = True


grid = ["SL","LR"]
print(solution(grid))