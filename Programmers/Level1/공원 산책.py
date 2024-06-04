def solution(park, routes):
    directions = {"N":[-1, 0], "S":[1, 0], "W":[0, -1], "E":[0, 1]}
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                start_x = i
                start_y = j
                break

    for i in routes:
        direct, dist = i.split()
        
        xx = start_x
        yy = start_y
        
        for j in range(int(dist)):
            nx = start_x + directions[direct][0]
            ny = start_y + directions[direct][1]
            
            if 0 <= nx <len(park) and 0 <= ny < len(park[0]) and park[nx][ny] != 'X':
                start_x = nx
                start_y = ny
                
            else:
                start_x = xx
                start_y = yy
                break
    
    return [start_x, start_y]

park = ["SOO","OOO","OOO"]
routes = ["E 2","S 2","W 1"]

print(solution(park, routes))