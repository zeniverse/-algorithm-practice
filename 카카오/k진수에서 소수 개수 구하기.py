import math

n = 110011
k = 10

def isPrime(x):
    if x == 1:
        return False
    
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True


num = ''
while n >= 1:
    n, b = divmod(n, k)
    num += str(b)

num = num[::-1]
arr = list(num.split('0'))

count = 0

for i in arr:
    if i != '':
        if isPrime(int(i)):
            count += 1

print(count)
