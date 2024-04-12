
while True:
    s = input()
    
    if s == '*':
        break

    for i in range(1, len(s) - 1):
        tmp = set()

        for j in range(len(s) - i):
            pair = s[j] + s[j + i]

            if pair in tmp:
                print(s, "is NOT surprising.")
                break
            else:
                tmp.add(pair)
        else:
            continue
        break
    else:
        print(s, "is surprising.")
