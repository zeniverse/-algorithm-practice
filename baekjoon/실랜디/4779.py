def cut(start, n):
    if n == 1:
        return
    
    for i in range(start + n // 3, start + (n // 3) * 2):
        res[i] = ' '
    
    cut(start, n // 3)
    cut(start + (n // 3) * 2, n // 3)

while True:
    try:
        n = int(input())
        res = ['-'] * (3**n)
        cut(0, 3**n)
        print(''.join(res))
    except:
        break