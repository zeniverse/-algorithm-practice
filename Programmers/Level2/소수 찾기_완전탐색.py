from itertools import permutations

numbers = "011"
numbers = list(numbers)

def isPrime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


tmp = []
res = 0

for i in range(1, len(numbers) + 1):
    tmp += list(permutations(numbers, i))


arr = set([int(''.join(t)) for t in tmp])

for i in arr:
    if isPrime(i):
        res += 1

print(res)
