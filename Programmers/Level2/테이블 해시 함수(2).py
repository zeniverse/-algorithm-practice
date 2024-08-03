from functools import reduce

data = [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]
col, row_begin, row_end = 2, 2, 3

def solution(data, col, row_begin, row_end):
    data = sorted(data, key=lambda x: (x[col - 1], -x[0]))
    return reduce(lambda x, y:x ^ y, [sum(map(lambda x: x % (i + 1), data[i])) for i in range(row_begin - 1, row_end)])

print(solution(data, col, row_begin, row_end))