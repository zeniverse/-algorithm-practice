
n = 5000
res = 0

while n != 1:
    if n == 2:
        break

    if n % 2 == 0:
        n //= 2
    else:
        n //= 2
        res += 1

print(res + 1)
