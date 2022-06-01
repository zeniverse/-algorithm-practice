import sys
input = sys.stdin.readline



a, b = input().split()

num_dict = dict()
count = 0
res = []

for i in range(0, 10):
    num_dict[str(i)] = i

for i in range(26):
    num_dict[chr(97 + i)] = i + 10

a_Max = max(list(a))
b_Max = max(list(b))

def trans(num, notation):
    num = num[::-1]
    tmp = 0

    for i in range(len(num)):
        tmp += (int(notation)**i) * num_dict[num[i]]

    return tmp


for i in range(num_dict[a_Max] + 1, 37):
    for j in range(num_dict[b_Max] + 1, 37):
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