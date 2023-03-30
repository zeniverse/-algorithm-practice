

def solution(park, routes):
    n = len(park)
    m = len(park[0])
    x, y = 0, 0

    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                x, y = i, j
                break

    for i in routes:
        a, b = x, y

        for j in range(int(i[2])):
            if i[0] == 'N' and a != 0 and park[a - 1][b] != 'X':
                a -= 1
                if j == int(i[2]) - 1:
                    x = a
            elif i[0] == 'S' and a != n - 1 and park[a + 1][b] != 'X':
                a += 1
                if j == int(i[2]) - 1:
                    x = a
            elif i[0] == 'W' and b != 0 and park[a][b - 1] != 'X':
                b -= 1
                if j == int(i[2]) - 1:
                    y = b
            elif i[0] == 'E' and b != m - 1 and park[a][b + 1] != 'X':
                b += 1
                if j == int(i[2]) - 1:
                    y = b
            print(x, y, '-----')
    
    return [x, y]

park = ["OSO","OOO","OXO","OOO"]
routes = ["E 2","S 3","W 1"]
print(solution(park, routes))