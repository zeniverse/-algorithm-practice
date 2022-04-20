import sys

n = int(sys.stdin.readline().strip())

arr = list(range(1, n + 1))
res = []

for i in range(len(arr)):
    tmp = list(map(int, str(arr[i])))
    tmp_num = arr[i]

    for j in range(len(tmp)):
        tmp_num += tmp[j]

    if tmp_num == n:
        res.append(arr[i])

if len(res) == 0:
    print(0)
else:
    print(min(res))


