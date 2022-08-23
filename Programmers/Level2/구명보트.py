
from collections import deque


people = [70, 50, 80, 50]
limit = 100

res = 0
queue = deque(sorted(people))

while queue:
    if len(queue) == 1:
        res += 1
        break

    if queue[0] + queue[-1] <= limit:
        queue.popleft()
        queue.pop()
    else:
        queue.pop()

    res += 1

print(res)





