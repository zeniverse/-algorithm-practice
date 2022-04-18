for _ in range(int(input())):
    n, s = input().split()

    for i in s:
        print(int(n) * i, end="")
    print()