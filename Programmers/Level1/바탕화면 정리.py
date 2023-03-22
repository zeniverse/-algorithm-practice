
def solution(wallpaper):
    arr = []

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                arr.append([i, j])

    a = min([i[0] for i in arr])
    b = min([i[1] for i in arr])
    c = max([i[0] for i in arr]) + 1
    d = max([i[1] for i in arr]) + 1
    
    return [a, b, c, d]

wallpaper = ["..", "#."]

print(solution(wallpaper))
