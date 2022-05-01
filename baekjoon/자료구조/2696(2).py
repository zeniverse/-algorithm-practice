import sys
input = sys.stdin.readline


for _ in range(int(input())):
    m = int(input())
    arr = []

    for i in range(m//10+1):
        arr.extend(list(map(int,input().split())))

    print(m//2 + 1)
    print(arr[0], end=" ")

    if m != 1:
        count = 1

        for i in range(2, m, 2):
            print(sorted(arr[:i + 1])[(i + 1)//2], end = " ")
            count += 1

            if count == 10:
                print()
                count = 0
        else:
            print()