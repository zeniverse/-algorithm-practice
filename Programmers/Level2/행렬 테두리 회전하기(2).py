
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

    for a, b, c, d in queries:
        stack = []
        r1, c1, r2, c2 = a - 1, b - 1, c - 1, d - 1

        for i in range(c1, c2 + 1):
            stack.append(arr[r1][i])

            if len(stack) == 1:
                continue
            else:
                arr[r1][i] = stack[-2]

        for j in range(r1 + 1, r2 + 1):
            stack.append(arr[j][i])
            arr[j][i] = stack[-2]

        for k in range(c2 - 1, c1 - 1, -1):
            stack.append(arr[j][k])
            arr[j][k] = stack[-2]

        for l in range(r2 - 1, r1 - 1, -1):
            stack.append(arr[l][k])
            arr[l][k] = stack[-2]

        res.append(min(stack))
        
    return res


print(solution(rows, columns, queries))