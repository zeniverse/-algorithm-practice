from itertools import combinations


line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]

def find_point(line1, line2):
    a, b, e = line1
    c, d, f = line2

    if a * d - b * c == 0:
        return 0.1, 0.1
    else:
        return (b * f - e * d)/(a * d - b * c), -(e*c - a*f)/(a*d - b*c)

def solution(line):
    points = []
    for combi in combinations(line, 2):
        x, y = find_point(combi[0], combi[1])
        
        if int(x) != x or int(y) != y:
            continue
        points.append([int(x), int(y)])

    print(points)

    x_dot = sorted([x for x, y in points])
    y_dot = sorted([y for x, y in points])
    w = x_dot[-1] - x_dot[0] + 1
    h = y_dot[-1] - y_dot[0] + 1

    print(x_dot)
    print(y_dot)

    # for i in range(len(points)):
    #     points[i][0] = points[i][0] - x_dot[0]
    #     points[i][1] = points[i][1] - y_dot[0]

    print(points)
    res = [["."] * w for _ in range(h)]
    for x, y in points:
        res[y - y_dot[0]][x - x_dot[0]] = "*"

    return [''.join(line) for line in res]

print(solution(line))