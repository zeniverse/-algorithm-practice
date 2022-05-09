from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(v, start, count):
    global cycle

    # 순환선인지 확인하는 과정
    # 시작역과 현재역이 같다면 && 2역 이상 지나왔다면 -> 순환선
    if start == v and count >= 2:
        cycle = True
        return

    visited[v] = True

    for e in adj[v]:
        if not visited[e]:
            dfs(e, start, count + 1)

        # 방문할 다음 역이 이미 방문처리 되어있을때
        # 순환인지 확인해야 하기 때문에 count를 그대로 유지해서 dfs를 실행한다.
        elif e == start and count >=2:
            dfs(e, start, count)

def bfs():
    global res

    queue = deque()

    for i in range(n):
        if isCycle[i]:
            res[i] = 0
            queue.append(i)

    while queue:
        current = queue.popleft()

        for e in adj[current]:
            if res[e] == -1:
                queue.append(e)
                res[e] = res[current] + 1

    for i in res:
        print(i, end=" ")


n = int(input())
adj = [[] for _ in range(n)]
isCycle = [False] * n
res = [-1] * n

for _ in range(n):
    a, b = map(int, input().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

for i in range(n):
    visited = [False] * n
    cycle = False
    dfs(i, i, 0)

    if cycle:
        isCycle[i] = True

bfs()