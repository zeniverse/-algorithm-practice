
import sys
input = sys.stdin.readline
INF = int(1e9)

def bf(start):
    distance = [INF] * (n + 1)
    distance[start] = 0

    for i in range(n):
        for edge in edges:
            current = edge[0]
            next_node = edge[1]
            cost = edge[2]

            if distance[next_node] > cost + distance[current]:
                distance[next_node] = cost + distance[current]

                if i == n - 1:
                    return True

    return False


for _ in range(int(input())):
    n, m, w = map(int, input().split())

    edges = []

    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
        edges.append((b, a, c))

    for _ in range(w):
        a, b, c = map(int, input().split())
        edges.append((a, b, -c))
    
    

    if bf(1):
        print("YES")
    else:
        print("NO")
