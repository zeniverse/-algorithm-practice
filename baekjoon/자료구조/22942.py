import sys

n = int(sys.stdin.readline())
arr = []
stack = []

for i in range(n):
    data = sys.stdin.readline().split()

    a = int(data[0]) - int(data[1])
    b = int(data[0]) + int(data[1])

    arr.append([a, i, 0])
    arr.append([b, i, 1])

arr.sort()

for i in range(n):
    check = arr[i][2]

    if check == 0:
        stack.append(arr[i])
    else:
        if stack[-1][2] == 0:
            if stack[-1][1] == arr[i][1]:
                stack.pop()
            else:
                print("NO")
                exit(0)

print("YES")