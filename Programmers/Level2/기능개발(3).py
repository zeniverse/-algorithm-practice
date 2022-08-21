import math

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

res = []

progresses = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]
front = 0

print(progresses)

for i in range(len(progresses)):
    if progresses[i] > progresses[front]:
        res.append(i - front)
        front = i
res.append(len(progresses) - front)

print(res)