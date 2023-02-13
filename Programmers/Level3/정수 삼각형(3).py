

def solution(triangle):

    length = len(triangle)

    while length > 1:
        for i in range(length - 1):
            triangle[length - 2][i] += max(triangle[length - 1][i], triangle[length - 1][i + 1])
        length -= 1

    return triangle
    

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))