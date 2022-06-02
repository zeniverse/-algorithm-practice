import sys, math
input = sys.stdin.readline

n = int(input())
a = set(list(map(int, input().split())))

# 숫자가 소수인지 확인하는 함수
def isPrime(num):
    if num == 0 or num == 1:
        return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

res = 1

# 소수들을 모두 곱해주는 과정
for i in a:
    if isPrime(i):
        res *= i

if res == 1:
    print(-1)
else:
    print(res)