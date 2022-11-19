import sys
input = sys.stdin.readline

n = int(input())
res = 0
arr = list(range(1, n + 1))

for i in arr:
    num = str(i)
    if len(num) <= 2:
        res += 1
    else:
        diff = int(num[0]) - int(num[1])
        flag = True
        for j in range(1, len(num) - 1):
            if int(num[j]) - int(num[j + 1]) != diff:
                flag = False

        if flag:
            res += 1

print(res)

