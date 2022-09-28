


def solution(info, edges):
    visited = [False] * len(info)
    visited[0] = True

    res = []

    def dfs(sheep, wolf):
        if sheep > wolf:
            res.append(sheep)
        else:
            return

        for parent, child in edges:
            isWolf = info[child]

            if visited[parent] and not visited[child]:
                visited[child] = True
                dfs(sheep + (isWolf == 0), wolf + (isWolf == 1))
                visited[child] = False

    dfs(1, 0)

    return max(res)

info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
print(solution(info, edges))