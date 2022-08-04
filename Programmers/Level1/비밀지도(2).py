n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]

res = []

for i, j in zip(arr1, arr2):
    num = bin(i|j)[2:]

    num = num.rjust(n, '0')
    num = num.replace('1', '#')
    num = num.replace('0', ' ')

    res.append(num)

print(res)










