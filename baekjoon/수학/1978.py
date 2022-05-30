import sys
input = sys.stdin.readline

def isPrime(num):
    if num == 1:
        return False

    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True

n = int(input())
arr = list(map(int, input().split()))
count = 0

for i in arr:
    if isPrime(i):
        count += 1

print(count)