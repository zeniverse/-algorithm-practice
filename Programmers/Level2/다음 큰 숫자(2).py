
n = 78

num1 = bin(n)
count1 = bin(n).count('1')

while True:
    n += 1

    if count1 == bin(n).count('1'):
        print(n)
        break


