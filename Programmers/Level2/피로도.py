
from copy import deepcopy
from itertools import permutations

dungeons = [[80,20],[50,40],[30,10]]
res = 0
k = 80

for permu in permutations(dungeons, len(dungeons)):
    n = deepcopy(k)
    count = 0
    for i in permu:
        if n < i[0]:
            continue
        else:
            n -= i[1]
            count += 1

    res = max(res, count)

print(res)