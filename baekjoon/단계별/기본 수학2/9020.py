import math

def getPrimeNum(num):
    arr = [True] * (num + 1)

    for i in range(2, int(math.sqrt(num)) + 1):
        if arr[i]:
            for j in range(i + i, num + 1, i):
                arr[j] = False

    return [i for i in range(2, num) if arr[i] == True]


for _ in range(int(input())):
    n = int(input())
    
    prime_num = getPrimeNum(n)

    half = n//2

    for i in range(half, 1, -1):
        if ((n - i) in prime_num) and (i in prime_num):
            print(i, n - i)
            break