from collections import deque
import sys
input = sys.stdin.readline

k = int(input())
queue = deque()

for _ in range(k):
    num = int(input())

    if num == 0:
        queue.pop()
    else:
        queue.append(num)

print(sum(queue))