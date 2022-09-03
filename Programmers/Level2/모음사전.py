
from itertools import product


word = "EIO"

res = []

for i in range(1, 6):
    for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
        res.append(''.join(c))

res.sort()
print(res.index(word) + 1)