for _ in range(int(input())):
    s = input()
    score = 0
    res = 0

    for i in s:
        if i == 'O':
            score += 1
            res += score
        else:
            score = 0
            res += score
    
    print(res)


