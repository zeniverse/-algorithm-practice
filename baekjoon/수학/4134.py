import sys, math
input = sys.stdin.readline

def isPrime(n):
    if n == 0 or n == 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for _ in range(int(input())):
    n = int(input())

    while True:
        if isPrime(n):
            print(n)
            break
        else:
            n += 1

    


