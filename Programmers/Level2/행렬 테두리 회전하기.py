
rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

def solution(rows, columns, queries):
    res = []
    arr = [[0 for _ in range(columns)] for _ in range(rows)]
    num = 1

    for row in range(rows):
        for col in range(columns):
            arr[row][col] = num
            num += 1

    for query in queries:
        query = [x - 1 for x in query]
        tmp = arr[query[0]][query[1]]
        ans = tmp

        # left
        for i in range(query[0] + 1, query[2] + 1):
            arr[i - 1][query[1]] = arr[i][query[1]]
            ans = min(ans, arr[i][query[1]])

        # bottom
        for i in range(query[1] + 1, query[3] + 1):
            arr[query[2]][i - 1] = arr[query[2]][i]
            ans = min(ans, arr[query[2]][i])

        # right
        for i in range(query[2] - 1, query[0] - 1, -1):
            arr[i + 1][query[3]] = arr[i][query[3]]
            ans = min(ans, arr[i][query[3]])

        # top
        for i in range(query[3] - 1, query[1] - 1, -1):
            arr[query[0]][i + 1] = arr[query[0]][i]
            ans = min(ans, arr[query[0]][i])

        arr[query[0]][query[1] + 1] = tmp
        res.append(ans)

    return res


print(solution(rows, columns, queries))