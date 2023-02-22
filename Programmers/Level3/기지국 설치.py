import math

def solution(n, stations, w):
    res = 0
    length = 1 + w * 2
    start = 1

    for station in stations:
        if station - w - start > 0:
            res += math.ceil((station - w - start)/length)
        start = station + w + 1
    
    if start <= n:
        res += math.ceil((n + 1 - start)/length)
    
    return res

n = 11
stations = [4, 11]
w = 1
print(solution(n, stations, w))
