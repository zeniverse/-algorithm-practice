from collections import deque

bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    w = 0

    while bridge:
        answer += 1
        w -= bridge.popleft()

        if truck:
            if w + truck[0] <= weight:
                t = truck.popleft()
                bridge.append(t)
                w += t
            else:
                bridge.append(0)
    return answer

print(solution(bridge_length, weight, truck_weights))