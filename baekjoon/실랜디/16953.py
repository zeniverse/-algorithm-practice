from collections import deque

a, b = map(int, input().split())
res = -1
queue = deque([(a, 1)])

while queue:
    i, count = queue.popleft()
    
    if i == b:
        res = count
        break

    if i * 2 <= b:
        queue.append((i * 2, count + 1))

    if int(str(i) + '1') <= b:
        queue.append((int(str(i) + '1'), count + 1))

print(res)