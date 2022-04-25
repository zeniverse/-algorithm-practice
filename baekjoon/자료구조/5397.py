import sys
n = int(sys.stdin.readline())

for _ in range(n):
    password = sys.stdin.readline().strip()
    left = []
    right = []

    for i in password:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)

    left.extend(right[::-1])
    print("".join(left))
    
