
def canVisitAllRooms(rooms):
    visited = [False] * len(rooms)

    def dfs(v):
        visited[v] = True

        for next in rooms[v]:
            if not visited[next]:
                dfs(next)

    dfs(0)

    return all(visited)

rooms = [[1, 3], [2, 4], [0], [4], [], [3, 4]]
print(canVisitAllRooms(rooms))