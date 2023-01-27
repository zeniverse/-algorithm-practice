

def solution(cap, n, deliveries, pickups):
    i, j = n -1, n - 1
    # i : 배달해야 하는 가장 먼 거리
    # j : 수거해야 하는 가장 먼 거리

    while i >= 0 and deliveries[i] == 0:
        i -= 1
    
    while j >= 0 and pickups[j] == 0:
        j -= 1

    res = 0

    while i >= 0 or j >= 0:
        res += (max(i, j) + 1) * 2

        # 배달
        cur = cap
        
        while i >= 0 and cur:
            if deliveries[i] > cur:
                deliveries[i] -= cur
                cur = 0
            else:
                cur -= deliveries[i]
                deliveries[i] = 0
                while i >= 0 and deliveries[i] == 0:
                    i -= 1

        # 수거
        cur = cap
        
        while j >= 0 and cur:
            if pickups[j] > cur:
                pickups[j] -= cur
                cur = 0
            else:
                cur -= pickups[j]
                pickups[j] = 0
                while j >= 0 and pickups[j] == 0:
                    j -= 1

    return res

cap, n = 4, 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]

print(solution(cap, n, deliveries, pickups))