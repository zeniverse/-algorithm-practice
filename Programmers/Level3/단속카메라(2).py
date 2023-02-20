

def solution(routes):
    routes.sort(key=lambda x: x[1])
    camera = -30000
    res = 0

    for route in routes:
        if camera < route[0]:
            res += 1
            camera = route[1]
    
    return res

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

print(solution(routes))

