

def solution(routes):
    routes.sort(key=lambda x: x[0], reverse = True)
    camera = route[0][0]
    res = 1

    for route in routes[1:]:
        if route[1] >= camera:
            continue
        else:
            camera = route[0]
            res += 1
    
    return res

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

print(solution(routes))

