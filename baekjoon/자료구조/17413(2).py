import sys

s = input()
tmp = ''
check = False

for i in s:
    if i == ' ':
        if not check:
           print(tmp[::-1], end = " ")
           tmp = ''
        else:
            print(i, end="")

    elif i == "<":
        print(tmp[::-1] + '<', end='')
        tmp = ''
        check = True

    elif i == '>':
        print(">", end='')
        check = False
    else:
        if check:
            print(i, end='')
        else:
            tmp += i

print(tmp[::-1])