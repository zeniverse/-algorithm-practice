import sys
input = sys.stdin.readline

a, b = input().split()
res = []
count = 0

for i in range(2, 37):
    try:
        a10 = int(a, i)
    except:
        continue

    for j in range(2, 37):
        try:
            b10 = int(b, j)

            if a10 == b10:
                if a10 >= 2**63:
                    continue
                count += 1
                res.append((a10, i, j))
        except:
            continue


if count == 1:
    print(*res[0])
elif count == 0:
    print("Impossible")
else:
    print("Multiple")

