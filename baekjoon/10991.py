n = int(input())

for i in range(1, n + 1):
    if i == n:
        print('*' + ' *' * (i - 1))
    else:
        print(' ' * (n - i - 1) + ' *' * i)