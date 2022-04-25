for _ in range(int(input())):
    n, findNum = map(int, input().split())
    arr = list(map(int, input().split()))
    stack = []
    count = 0
    end = False

    for i, importance in enumerate(arr):
        stack.append((i, importance))

    

    while not end:
        max_importance = max(stack, key=lambda x: x[1])[1]

        for i in range(0,len(stack)):
            if stack[i][1] == max_importance:
                count += 1

                if stack[i][0] == findNum:
                    print(count)
                    end = True
                else:
                    stack.pop(i)
                break
            else:
                stack.append(stack.pop(i))
                break

    
