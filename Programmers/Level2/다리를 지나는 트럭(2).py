
from collections import deque


bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]

res = 0

current_weigt = 0
bridge_weight = deque([0] * bridge_length)
trucks = deque(truck_weights)

while trucks or current_weigt > 0:
    removedTruck = bridge_weight.popleft()
    current_weigt -= removedTruck

    if trucks and current_weigt + trucks[0] <= weight:
        newTruck = trucks.popleft()
        current_weigt += newTruck

        bridge_weight.append(newTruck)

    else:
        bridge_weight.append(0)

    res += 1


print(res)


