import sys, math
input = sys.stdin.readline

def isPrime(num):
    if num == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if num % i == 0:
            return False

    return True


n = int(input())

while True:
    if isPrime(n):
        if str(n) == str(n)[::-1]:
            print(n)
            break

    n += 1