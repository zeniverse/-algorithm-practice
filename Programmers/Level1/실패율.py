n = 4
stages = [1,2,3,2,1]

users = len(stages)
fail = []

for stage in range(1, n + 1):
    count = stages.count(stage)

    if users == 0:
        fail.append((stage, 0))
    else:
        fail.append((stage, count / users))

    users -= count

fail.sort(key=lambda x: (-x[1], x[0]))

print([i[0] for i in fail])
