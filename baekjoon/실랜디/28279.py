from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
queue = deque([])

for _ in range(n):
    num = list(map(int, input().strip().split()))

    if num[0] == 1:
        queue.appendleft(num[1])
    elif num[0] == 2:
        queue.append(num[1])
    elif num[0] == 3:
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif num[0] == 4:
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif num[0] == 5:
        print(len(queue))
    elif num[0] == 6:
        if queue:
            print(0)
        else:
            print(1)
    elif num[0] == 7:
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)