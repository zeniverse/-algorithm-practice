from collections import defaultdict
from datetime import datetime
import math

fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]

cars = defaultdict(list)
res = []

for i in records:
    record = i.split()
    cars[record[1]].append((record[0], record[2]))

cars = dict(sorted(cars.items(), key=lambda x : x[0]))

for k, v in cars.items():
    if len(cars[k]) % 2 != 0:
        cars[k].append(("23:59", "OUT"))

    time = 0
    for i in range(0, len(v), 2):
        tmp = datetime.strptime(v[i + 1][0], "%H:%M") - datetime.strptime(v[i][0], "%H:%M")
        time += tmp.seconds//60

    if time <= fees[0]:
        res.append(fees[1])
    else:
        total = fees[1] + (math.ceil((time - fees[0])/fees[2])) * fees[3]
        res.append(total)

print(res)