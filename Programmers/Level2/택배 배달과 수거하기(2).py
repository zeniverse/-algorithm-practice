from itertools import zip_longest

def tolist(arr):
    n = []
    for idx, d in enumerate(arr):
        for _ in range(d):
            n.append(idx + 1)
    return n

def solution(cap, n, deliveries, pickups):
    
    deliveries = tolist(deliveries)
    pickups = tolist(pickups)

    deliveries.reverse()
    pickups.reverse()

    deliveries = deliveries[::cap]
    pickups = pickups[::cap]
    
    return 2 * sum([max(x, y) for x, y in zip_longest(deliveries, pickups, fillvalue=0)])

cap, n = 4, 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]

print(solution(cap, n, deliveries, pickups))