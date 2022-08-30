
dirs = "ULURRDLLU"

check = set()
x, y = 5, 5

move = {'U':(0, -1), 'D':(0, 1), 'R' : (1, 0), 'L':(-1, 0)}

for i in range(len(dirs)):
    nx = x + move[dirs[i]][0]
    ny = y + move[dirs[i]][1]

    if nx < 0 or nx > 10 or ny < 0 or ny > 10:
        continue

    check.add((x, y, nx, ny))
    check.add((nx, ny, x, y))

    x, y = nx, ny

res = len(check)//2



print(res)

