
dungeons = [[80,20],[50,40],[30,10]]
k = 80

N = 0
res = 0
visited = []

def dfs(k, count, dungeons):
    global res

    if count > res:
        res = count

    for i in range(N):
        if k >= dungeons[i][0] and not visited[i]:
            visited[i] = True
            dfs(k - dungeons[i][1], count + 1, dungeons)
            visited[i] = False



def solution(k, dungeons):
    global N, visited

    N = len(dungeons)
    visited = [False] * N

    dfs(k, 0, dungeons)

    return res


print(solution(k, dungeons))