from collections import deque
import sys

d = deque()

for _ in range(int(sys.stdin.readline().strip())):
    order = sys.stdin.readline().strip().split()

    if order[0] == 'push_front':
        d.appendleft(order[1])
    
    elif order[0] == 'push_back':
        d.append(order[1])

    elif order[0] == 'pop_front':
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())

    elif order[0] == 'pop_back':
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())

    elif order[0] == 'size':
        print(len(d))

    elif order[0] == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)

    elif order[0] == 'front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    
    elif order[0] == 'back':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
