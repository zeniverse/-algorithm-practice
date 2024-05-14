for _ in range(int(input())):
    s, p = input().split()

    s = s.replace(p,"1")
    print(len(s))
    