
dots = [[1, 4], [9, 2], [3, 8], [11, 6]]

def solution(dots):
    for a, b, c, d in [(0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)]:
        m1 = (dots[b][1] - dots[a][1]) / (dots[b][0] - dots[a][0])
        m2 = (dots[d][1] - dots[c][1]) / (dots[d][0] - dots[c][0])

        if m1 == m2:
            return 1
    return 0
    

print(solution(dots))