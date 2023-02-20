

def solution(routes):
    routes.sort(key=lambda x: x[1])
    cameras = [routes[0][1]]

    for i in range(1, len(routes)):
        if routes[i][0] <= cameras[-1] and routes[i][1] >= cameras[-1]:
            continue
        else:
            cameras.append(routes[i][1])
    
    return len(cameras)

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

print(solution(routes))

