import sys

arr = list(sys.stdin.readline().strip())

res = []
tmp = ''
check = True

for i in range(len(arr)):
    
    if arr[i] == '<':
        if len(tmp) != 0:
            res.append(tmp[::-1])
            tmp=''

        tmp += arr[i]
        check = False

    elif arr[i] == '>':
        tmp += arr[i]
        res.append(tmp)
        tmp = ''
        check = True

    elif arr[i] == ' ':
        if check:
            res.append(tmp[::-1])
            res.append(arr[i])
            tmp = ''
        else:
            tmp += arr[i]

    elif i == len(arr) -1:
        tmp += arr[i]
        res.append(tmp[::-1])

    else:
        tmp += arr[i]


for i in res:
    print(i, end='')