import sys
input = sys.stdin.readline

n, p = map(int, input().split())
arr = [[] for _ in range(7)]
res = 0

for _ in range(n):
    line, pnum = map(int, input().split())

    if not arr[line]:
        arr[line].append(pnum)
        res += 1
    else:
        if pnum > arr[line][-1]:
            arr[line].append(pnum)
            res += 1
        elif pnum < arr[line][-1]:
            while True:
                if not arr[line] or pnum > arr[line][-1]:
                    arr[line].append(pnum)
                    res += 1
                    break
                elif pnum == arr[line][-1]:
                    break
                else:
                    arr[line].pop()
                    res += 1

print(res)






