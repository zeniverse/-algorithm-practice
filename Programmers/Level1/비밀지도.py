n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]

res = [ 0 for _ in range(n)]

for i in range(n):
    tmp1 = format(arr1[i], 'b')
    tmp2 = format(arr2[i], 'b')
    arr1[i] = '0' * (n - len(tmp1)) + str(tmp1)
    arr2[i] = '0' * (n - len(tmp2)) + str(tmp2)

for i in range(n):
    tmp = ''
    for j in range(n):
        if arr1[i][j] == '1' or arr2[i][j] == '1':
            tmp += '#'
        else:
            tmp += ' '

    res[i] = tmp

print(res)










