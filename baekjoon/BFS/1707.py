from collections import deque

def bfs(num):
    queue = deque([num])
    visited[num] = 1

    while queue:
        x = queue.popleft()

        for i in adj[x]:
            if visited[i] == 0:
                visited[i] = -visited[x]
                queue.append(i)
            else:
                if visited[i] == visited[x]:
                    return False
    return True


for _ in range(int(input())):
    v, e = map(int, input().split())
    adj = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)
    flag = 1

    for _ in range(e):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    for i in range(1, v + 1):
        if visited[i] == 0:
            if not bfs(i):
                flag = -1
                break

    print('YES' if flag == 1 else 'NO')