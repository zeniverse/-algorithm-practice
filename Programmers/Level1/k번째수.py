array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
res = []

for command in commands:
    i, j, k = command
    tmp = sorted(array[i-1:j])

    res.append(tmp[k - 1])

print(res)

