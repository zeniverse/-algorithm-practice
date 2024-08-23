
# 행렬 테두리 회전하기(1)과 비슷하지만,
# 좀 더 가독성 있음

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

def solution(rows, columns, queries):
    answer = []
    arr = [[0] * columns for _ in range(rows)]
    num = 1

    for i in range(rows):
        for j in range(columns):
            arr[i][j] = num
            num += 1


    for query in queries:
        x1, y1, x2, y2 = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
        min_num = arr[x1][y1]
        tmp = arr[x1][y1]

        # left
        for i in range(x1, x2):
            move = arr[i + 1][y1]
            arr[i][y1] = move
            min_num = min(min_num, move)

        # bottom
        for i in range(y1, y2):
            move = arr[x2][i + 1]
            arr[x2][i] = move
            min_num = min(min_num, move)

        # right
        for i in range(x2, x1, -1):
            move = arr[i - 1][y2]
            arr[i][y2] = move
            min_num = min(min_num, move)

        # top
        for i in range(y2, y1, -1):
            move = arr[x1][i - 1]
            arr[x1][i] = move
            min_num = min(min_num, move)

        arr[x1][y1 + 1] = tmp
        answer.append(min_num)

    return answer


print(solution(rows, columns, queries))