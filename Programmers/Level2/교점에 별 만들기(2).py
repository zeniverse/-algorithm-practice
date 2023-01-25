from itertools import combinations


line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]


def solution(line):
    points = set()
    maxX, maxY, minX, minY = -10e10, -10e10, 10e10, 10e10

    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]

            tmp = a * d - b * c

            if tmp != 0 and (b * f - e * d) % tmp == 0 and (e * c - a * f) % tmp == 0:
                x = (b * f - e * d) // tmp
                y = (e * c - a * f) // tmp

                maxX, maxY, minX, minY = max(maxX, x), max(maxY, y), min(minX, x), min(minY, y)
                points.add((x, y))

    print(points)
    print(maxX, minX, maxY, minY)

    res = [["." for _ in range(maxX - minX + 1)] for _ in range(maxY - minY + 1)]

    for x, y in points:
        res[maxY - y][x - minX] = '*'

    return ["".join(row) for row in res]

print(solution(line))