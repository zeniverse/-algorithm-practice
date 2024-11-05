from collections import deque

def canVisitAllRooms(rooms):
    visited = [False] * len(rooms)

    def bfs(v):
        queue = deque([v])
        visited[v] = True

        while queue:
            cur = queue.popleft()

            for next in rooms[cur]:
                if not visited[next]:
                    visited[next] = True
                    queue.append(next)
    bfs(0)

    return all(visited)

rooms = [[1, 3], [2, 4], [0], [4], [], [3, 4]]
print(canVisitAllRooms(rooms))