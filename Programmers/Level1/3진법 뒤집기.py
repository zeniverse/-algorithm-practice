
n = 45

tmp = ''

while n:
    tmp += str(n%3)
    n = n //3

print(int(tmp, 3))

