n = int(input())

def star(start, end, add):
    length = n * 2
    for i in range(start, end, add):
        print('*' * i + ' ' * (length - 2*i) + '*'*i)

star(1, n + 1, 1)
star(n - 1, 0, -1)

