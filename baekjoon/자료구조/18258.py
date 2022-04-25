from collections import deque
import sys

n = int(sys.stdin.readline().strip())
d = deque()

for _ in range(n):
    order = sys.stdin.readline().strip().split()

    if order[0] == 'push':
        d.append(order[1])
    elif order[0] == 'pop':
        if d:
            print(d[0])
            d.popleft()
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(d))
    elif order[0] == 'empty':
        if d:
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if d:
            print(d[0])
        else:
            print(-1)
    else:
        if d:
            print(d[-1])
        else:
            print(-1)