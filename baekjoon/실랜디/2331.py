a, p = map(int, input().split())
arr = [a]

while True:
    num = arr[-1]

    tmp = 0
    for i in str(num):
        tmp += int(i) ** p

    if tmp in arr:
        print(arr.index(tmp))
        break
    else:
        arr.append(tmp)

