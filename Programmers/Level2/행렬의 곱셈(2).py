arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

def solution(arr1, arr2):
    n, m, r = len(arr1), len(arr1[0]), len(arr2[0])
    answer = [[0 for _ in range(r)] for _ in range(n)]

    for i in range(n):
        for k in range(r):
            for j in range(m):
                answer[i][k] += answer[i][j] + answer[j][k]

    return answer

print(solution(arr1, arr2))