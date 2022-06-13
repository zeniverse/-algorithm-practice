import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x):
    global res

    visited[x] = True
    # cycle 리스트에 값을 넣어서 다시 되돌아 오는지 확인해준다
    # (사이클을 형성하는지 확인)
    cycle.append(x)
    num = arr[x]

    # 이미 방문한 노드의 경우
    if visited[num]:
        if num in cycle:
            # 사이클의 시작점인 num의 인덱스부터 나머지를
            # res 리스트에 더해준다.
            res += cycle[cycle.index(num):]
            return
    else:
        dfs(num)


for _ in range(int(input())):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)

    # 팀이 된 학생 리스트 (사이클을 형성하는 수)
    res = []

    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - len(res))
