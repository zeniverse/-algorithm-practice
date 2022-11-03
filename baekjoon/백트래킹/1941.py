import sys
input = sys.stdin.readline

lst = [list(input().rstrip()) for _ in range(5)]

visited = [[0] * 5 for _ in range(5)]
res = 0
arr = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def check(n):
    global visited

    # n -> 5*5 배열을 25칸짜리 1차원 배열로 나타냈을 때, 첫번째 칠공주의 위치
    x = n % 5
    y = n // 5

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue
            
        if not visited[nx][ny]:
            # 좌표로 변경한 nx, ny를 다시 1차원 배열로 만드는 방법
            # (y좌표 * 5 + x좌표)
            if (ny * 5 + nx) in arr:
                visited[nx][ny] = 1
                check(ny * 5 + nx)



def dfs(cnt, idx, ycnt):
    global res, visited

    # 가지치기를 위해 'Y'가 4개 이상이거나,
    # 남은 사람의 명수가 필요로하는 갯수보다 적으면 가지치기!
    if ycnt >= 4 or 25 - idx < 7 - cnt:
        return

    # 7명이 모여졌다면, 인접한 자리끼리 모인건지 확인
    if cnt == 7:
        check(arr[0])

        if sum(sum(visited, [])) == 7:
            res += 1

        # 매 경우마다 visited를 새롭게 갱신해준다
        visited = [[0] * 5 for _ in range(5)]
        return


    # 5*5 행렬을 a[25]로(일자로) 구현하기 때문에
    # 좌표를 알기 위해서 진행하는 과정
    x = idx % 5
    y = idx // 5

    arr.append(idx)
    
    if lst[x][y] == 'Y':
        dfs(cnt + 1, idx + 1, ycnt + 1)
    else:
        dfs(cnt + 1, idx + 1, ycnt)

    # 이번 학생은 칠공주 멤버로 넣지 않는 경우
    # 다음 학생을 확인하기 위해 idx만 +1 해준다
    arr.pop()
    dfs(cnt, idx + 1, ycnt)


dfs(0, 0, 0)
print(res)

    


