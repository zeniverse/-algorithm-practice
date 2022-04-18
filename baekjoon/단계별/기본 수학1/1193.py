import sys

x = int(sys.stdin.readline())
check = 0
num = 0

while x > num:
    check += 1
    num += check

gap = num - x

if check % 2 == 0:
    top = check - gap
    bottom = gap + 1
else:
    top = gap + 1
    bottom = check - gap

print(f'{top}/{bottom}')