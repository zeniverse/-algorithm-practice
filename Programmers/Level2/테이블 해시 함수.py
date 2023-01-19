
data = [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]
col, row_begin, row_end = 2, 2, 3

def solution(data, col, row_begin, row_end):
    res = 0

    data = sorted(data, key=lambda x: (x[col - 1], -x[0]))

    
    for i in range(row_begin - 1, row_end):
        num = 0
        for j in range(len(data[i])):
            num += data[i][j] % (i + 1)
        res = res ^ num

    return res

print(solution(data, col, row_begin, row_end))