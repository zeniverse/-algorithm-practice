import sys

arr = []

for _ in range(int(input())):
    order = sys.stdin.readline().strip().split()

    if len(order) >= 2:
        arr.append(order[1])

    elif 'pop' == order[0]:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop(-1))

    elif 'size' == order[0]:
        print(len(arr))

    elif 'empty' == order[0]:
        if len(arr) == 0:
            print(1)
        else:
            print(0)

    elif 'top' == order[0]:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
