
k = 5
ranges = [[0,0],[0,-1],[2,-3],[3,-3]]

def solution(k, ranges):
    res = []
    inttegralArea = [0.0]

    while k != 1:
        newK = (k // 2) if k % 2 == 0 else (k * 3) + 1

        # 0 부터 newK 까지의 정적분 넓이
        # 범위를 반으로 잘라 아래 사각형 + 위에 삼각형 넓이 합으로 그래프의 넓이를 구한다
        minY, maxY = min(k, newK), max(k, newK)
        inttegralArea.append(inttegralArea[-1] + (minY + (1/2) * (maxY - minY)))

        k = newK

    length = len(inttegralArea)

    for y1, y2 in ranges:
        if length + (y2 - 1) >= y1:
            res.append(inttegralArea[y2 - 1] - inttegralArea[y1])
        else:
            res.append(-1)

    return res

print(solution(k, ranges))