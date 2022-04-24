
while True:
    try:
        s = input()
        res = [0] * 4

        for i in s:
            if i.isalpha():
                if i.islower():
                    res[0] += 1
                else:
                    res[1] += 1
            elif i.isdigit():
                res[2] += 1
            else:
                res[3] += 1

        print(*res)
    except:
        break

