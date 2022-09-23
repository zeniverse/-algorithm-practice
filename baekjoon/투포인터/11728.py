import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res =[]

a_pointer = 0
b_pointer = 0

while a_pointer != len(a) or b_pointer < len(b):

    if a_pointer == len(a):
        res.append(b[b_pointer])
        b_pointer += 1

    elif b_pointer == len(b):
        res.append(a[a_pointer])
        a_pointer += 1

    else:
        if a[a_pointer] < b[b_pointer]:
            res.append(a[a_pointer])
            a_pointer += 1
        else:
            res.append(b[b_pointer])
            b_pointer += 1

print(*res)