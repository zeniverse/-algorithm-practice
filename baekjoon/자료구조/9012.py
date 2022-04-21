for _ in range(int(input())):
    arr = list(input())
    
    sum = 0

    for i in arr:
        if i == '(':
            sum += 1

        elif i == ')':
            sum -= 1

        if sum < 0:
            print('NO')
            break

    if sum >= 1:
        print("NO")
    elif sum == 0:
        print("YES")
