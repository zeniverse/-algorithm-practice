for _ in range(int(input())):
    n, findNum = map(int, input().split())
    arr = list(map(int, input().split()))
    stack = []
    count = 0

    for i, importance in enumerate(arr):
        stack.append((i, importance))

    while True:
        if stack[0][1] == max(stack, key = lambda x:x[1])[1]:
            count += 1

            if stack[0][0] == findNum:
                print(count)
                break
            else:
                stack.pop(0)
        else:
            stack.append(stack.pop(0))

    
