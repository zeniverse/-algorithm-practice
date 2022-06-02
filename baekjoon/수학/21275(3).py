import sys
input = sys.stdin.readline

a, b = input().split()

nums = "0123456789abcdefghijklmnopqrstuvwxyz"
count = 0
res = []

a_Max = nums.index(max(list(a)))
b_Max = nums.index(max(list(b)))

def trans(num, notation):
    num = num[::-1]
    tmp = 0

    for i in range(len(num)):
        tmp += (int(notation)**i) * nums.index(num[i])

    return tmp


for i in range(a_Max + 1, 37):
    for j in range(b_Max + 1, 37):
        if i == j:
            continue

        if trans(a, i) == trans(b, j):
            if trans(a, i) >= 2**63:
                continue

            res.append((trans(a, i), i, j))
            count += 1

if count == 1:
    print(*res[0])
elif count > 1:
    print("Multiple")
else:
    print("Impossible")