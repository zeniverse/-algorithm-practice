import sys, math
input = sys.stdin.readline

def isPrime(num):
    if num == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if num % i == 0:
            return False

    return True

def isPalindrome(num):
    if str(num) == str(num)[::-1]:
            return True
    return False


n = int(input())

while True:
    if isPalindrome(n):
        if isPrime(n):
            print(n)
            exit(0)
    n += 1
