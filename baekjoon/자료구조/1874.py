n = int(input())
stack = []
res = []
count = 1

for _ in range(n):
    data = int(input())

    while data >= count:
        stack.append(count)
        res.append('+')
        count += 1

    if data == stack[-1]:
        stack.pop()
        res.append('-')
    else:
        print('NO')
        exit(0)

for i in res:
    print(i)

    

    

