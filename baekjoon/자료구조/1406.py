import sys

left = list(sys.stdin.readline().strip())
right = []
n = int(sys.stdin.readline().strip())

for _ in range(n):
    order = sys.stdin.readline().strip().split()

    if order[0] == 'L':
        if len(left) != 0:
            right.append(left.pop())

    elif order[0] == 'D':
        if len(right) != 0:
            left.append(right.pop())

    elif order[0] == 'B':
        if len(left) != 0:
            left.pop()

    else:
        left.append(order[1])

left.extend(right[::-1])

print("".join(left))