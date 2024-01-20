
while True:
    try:
        a, b = input().split()

        idx = 0
        flag = False
        for i in range(len(b)):
            if b[i] == a[idx]:
                idx += 1

                if idx == len(a):
                    flag = True
                    break
        if flag:
            print("Yes")
        else:
            print("No")
    except:
        break
