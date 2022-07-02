from collections import deque

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"

l_num = [1,4,7]
r_num = [3,6,9]

location = [[1,2,3],[4,5,6],[7,8,9],['*', 0, '#']]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(start, end):
    visited = [[-1] * 3 for _ in range(4)]

    for i in range(4):
        for j in range(3):
            if location[i][j] == start:
                start_x = i
                start_y = j
            
            if location[i][j] == end:
                end_x = i
                end_y = j


    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 0

    while queue:
        x, y = queue.popleft()

        if x == end_x and y == end_y:
            return visited[x][y]


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= 4 or ny < 0 or ny >= 3:
                continue

            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

left_location = '*'
right_location = '#'

res = ""

for i in numbers:
    if i in l_num:
        res += 'L'
        left_location = i
    elif i in r_num:
        res += 'R'
        right_location = i
    else:
        l_distance = bfs(left_location, i)
        r_distance = bfs(right_location, i)

        if l_distance < r_distance:
            res += 'L'
            left_location = i
        elif r_distance < l_distance:
            res += 'R'
            right_location = i
        else:
            if hand[:1] == 'r':
                res += 'R'
                right_location = i
            else:
                res += 'L'
                left_location = i

print(res)