
bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]

res = 0

bridge_weight = [0] * bridge_length


while bridge_weight:
    res += 1
    bridge_weight.pop(0)

    if truck_weights:
        if sum(bridge_weight) + truck_weights[0] <= weight:
            bridge_weight.append(truck_weights.pop(0))

        else:
            bridge_weight.append(0)

print(res)