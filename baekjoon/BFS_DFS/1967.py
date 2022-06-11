from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))


def bfs(v):
    maxNode, maxCost = 0, 0
    queue = deque()
    queue.append((v, 0))

    visited = [False] * (n + 1)
    visited[v] = 1

    while queue:
        v, cost = queue.popleft()

        for i in tree[v]:
            a, b = i
            if visited[a] == 0:
                visited[a] = 1
                queue.append((a, cost + b))

                if cost + b > maxCost:
                    maxCost = cost + b
                    maxNode = a
                    
    return maxNode, maxCost


# 루트 노드에서 가장 먼 노드 찾기
node, cost = bfs(1)

# 가장 먼 노드(start)에서 가장 먼 노드 찾기
resNode, result = bfs(node)
print(result)