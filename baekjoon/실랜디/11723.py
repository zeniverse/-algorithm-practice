import sys
input = sys.stdin.readline

m = int(input())
s = set()

for _ in range(m):
    str = input().strip().split()
    order = str[0]

    if order == 'add':
        s.add(int(str[1]))
    elif order == 'remove':
        s.discard(int(str[1]))
    elif order == 'check':
        if int(str[1]) in s:
            print(1)
        else:
            print(0)
    elif order == 'toggle':
        if int(str[1]) in s:
            s.discard(int(str[1]))
        else:
            s.add(int(str[1]))
    elif order == 'all':
        s = set(range(1, 21))
    else:
        s = set()