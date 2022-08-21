n = 15
res = ''

while n:
    if n % 3:
        res += str(n % 3)
        n //= 3
    else:
        res += '4'
        n = (n // 3) - 1

print(res[::-1])

