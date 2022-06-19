import sys
input = sys.stdin.readline
INF = int(1e9)

def bf(start):
    dist[start] = 0

    # 전체 n번의 라운드를 반복
    for i in range(n):
        # 매 반복마다 모든 간선을 화인
        for j in range(m):
            current = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]

            if dist[current] != INF and dist[next_node] > dist[current] + cost:
                dist[next_node] = dist[current] + cost

                # n - 1번째도 값이 변한다면 음수 간선 순환이 존재한다는 뜻
                if i == n - 1:
                    return True

    return False

n, m = map(int, input().split())
edges = []
dist = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

negative_cycle = bf(1)

if negative_cycle:
    # 음수 간선 순환이 존해하는 경우
    print("-1")
else:
    for i in range(2, n + 1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])