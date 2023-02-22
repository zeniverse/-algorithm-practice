
def solution(n, stations, w):
    res = 0
    idx = 0
    current = 1

    while current <= n:
        if idx < len(stations) and current >= stations[idx] - w:
            current = stations[idx] + w + 1
            idx += 1
        else:
            current += 1 + 2 * w
            res += 1

    return res

n = 11
stations = [4, 11]
w = 1
print(solution(n, stations, w))
