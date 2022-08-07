
dartResult = '1D#2S*3S'
res = []
tmp = dartResult[0]

for i in range(1, len(dartResult)):
    if dartResult[i].isdigit() and tmp != '':
        if dartResult[i - 1].isdigit():
            tmp += dartResult[i]
        else:
            res.append(tmp)
            tmp = dartResult[i]
    elif dartResult[i] == 'S':
        tmp = int(tmp) ** 1
    elif dartResult[i] == 'D':
        tmp = int(tmp) ** 2
    elif dartResult[i] == 'T':
        tmp = int(tmp) ** 3
    elif dartResult[i] == '*':
        if res:
            res[-1] = res[-1] * 2
        tmp = tmp * 2
    elif dartResult[i] == "#":
        tmp = tmp * (-1)
    else:
        tmp += dartResult[i]
res.append(tmp)

print(sum(res))



