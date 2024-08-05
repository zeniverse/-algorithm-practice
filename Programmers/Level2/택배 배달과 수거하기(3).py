

def solution(cap, n, deliveries, pickups):
    answer = 0
    d = 0
    p = 0

    for i in range(n - 1, -1, -1):
        d += deliveries[i]
        p += pickups[i]

        while d > 0 or p > 0:
            d -= cap
            p -= cap
            answer += (i + 1) * 2

    return answer

cap, n = 4, 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]

print(solution(cap, n, deliveries, pickups))