from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)


def solution(edges):
    nodes = set() # 모든 노드 담기
    conn = defaultdict(list) #나한테서 나가는 간선
    reverse_conn = defaultdict(list) #나한테 들어오는 간선

    for a, b in edges:
        nodes.add(a)
        nodes.add(b)
        conn[a].append(b) # a -> b
        reverse_conn[b].append(a) # b <- a


    # 생성된 노드 판단

    # 생성된 노드는 나에게 들어오는 화살표는 0개 이면서 나한테서 나가는 화살표는 2개 이상이어야 한다
    # 나에게 들어오는 화살표가 0개인 경우는 두가지가 있는데
    # 1. 직선 그래프 일때의 시작 노드
    # 2. 생성된 노드
    # 1번의 경우엔 나가는 화살표가 1개이므로 걸러낼 수 있음!
    def get_generated_node():
        for node in nodes:
            if len(reverse_conn[node]) > 0:
                continue
            elif len(conn[node]) < 2:
                continue
            return node
        
    gn = get_generated_node()
    graph_nodes = [n for n in conn[gn]] #2, 8, 7
    visited = set()

    def search(node):
        if node not in conn or len(conn[node]) == 0:
            # 해당 노드에서 나가는 간선이 없으면 무조건 막대(사이클이 없음)
            return "막대"
        elif node in visited:
            # 이미 방문을 했던 노드면 도넛
            return "도넛"

        # 나한테서 나가는 애
        if len(conn[node]) >= 2:
            return "8자"
        # 나에게로 들어오는 애 (생성된 노드에서 뻗어나온 화살표는 제외해야 됨)]
        if node in reverse_conn:
            in_arrow = [i for i in reverse_conn[node] if i != gn]
            if len(in_arrow) >= 2:
                return "8자" 

        nxt = conn[node][0]
        visited.add(node)
        return search(nxt)

    answer = [gn, 0, 0, 0] # 생성된 노드 번호, 막대 갯수, 도넛 갯수, 8자 갯수
    for graph_node in graph_nodes:
        result = search(graph_node)
        if result == "도넛":
            answer[1] += 1
        elif result == "막대":
            answer[2] += 1
        elif result == "8자":
            answer[3] += 1

    return answer

edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
print(solution(edges))