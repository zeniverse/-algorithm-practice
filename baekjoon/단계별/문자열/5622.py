arr = [(2, 'ABC'), (3, 'DEF'), (4, 'GHI'), (5, 'JKL'), (6, 'MNO'), (7, 'PQRS'), (8, 'TUV'), (9, 'WXYZ')]
s = input()
res = 0

for i in s:
    for j in range(len(arr)):
        if i in arr[j][1]:
            res += int(arr[j][0]) + 1

print(res)
            