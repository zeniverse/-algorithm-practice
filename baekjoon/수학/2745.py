n, b = input().split()
n = n[::-1]
b = int(b)

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

res = 0

for i in range(len(n)-1, -1, -1):
    sum = number.index(n[i]) * (b ** i)
    res += sum

print(res)
