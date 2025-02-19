
line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]


def solution(line):
    answer = []
    points = set()

    # 교점 구하기
    # Ax + By + E = 0
    # Cx + Dy + F = 0
    # x좌표 = BF-ED / AD-BC
    # y좌표 = EC-AF / AD-BC
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]

            if (a * d) - (b * c) != 0:
                x = (b * f - e * d) / (a * d - b * c)
                y = (e * c - a * f) / (a * d - b * c)

            # 정수 확인
            if int(x) == x and int(y) == y:
                points.add((int(x), int(y)))

    # 그림 그릴 영역 구하기
    min_x = min(point[0] for point in points)
    max_x = max(point[0] for point in points)
    min_y = min(point[1] for point in points)
    max_y = max(point[1] for point in points)

    # 그림 그리기
    # x 좌표는 왼쪽에서 오른쪽으로 증가하고
    # y 좌표는 위에서 아래로 감소하기 때문에 y값은 max값에서부터 내려온다
    for y in range(max_y, min_y - 1, -1):
        row = ""
        for x in range(min_x, max_x + 1):
            if (x, y) in points:
                row += "*"
            else:
                row += "."

        answer.append(row)
    
    return answer

print(solution(line))