
res = []

while True:
    s = input()
    stack = []
    count = 0

    if '-' in s:
        break

    for i in s:
        if i == '{':
            stack.append(i)
        elif not stack and i == '}':
            count += 1
            stack.append('{')
        elif stack and i == '}':
            stack.pop()

    count += len(stack) // 2
    res.append(count)

for i in range(len(res)):
    print(i + 1, '. ', res[i], sep='')


