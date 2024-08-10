
arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]


def solution(arr):

    def encode(x, y, l):
        check = arr[x][y]
        for i in range(x, x + l):
            for j in range(y, y + l):
                if arr[i][j] != check:
                    encode(x, y, l // 2)
                    encode(x, y + l // 2, l // 2)
                    encode(x + l // 2, x, l // 2)
                    encode(x + l // 2, y + l // 2, l // 2)
                    return
        else:
            answer[check] += 1


    answer = [0, 0]
    encode(0, 0, len(arr))

    return answer

print(solution(arr))




