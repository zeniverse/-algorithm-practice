N = 4
stages = [1,2,3,2,1]

fail = []
info = [0] * (N + 2)

for stage in stages:
    info[stage] += 1

for i in range(1, N + 1):
    total = sum(info[i:])
    current = info[i]

    if total == 0:
        fail.append((i, 0))
    else:
        fail.append((i, current / total))

fail.sort(key=lambda x : (-x[1], x[0]))

print([i[0] for i in fail])
