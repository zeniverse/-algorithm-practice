n = int(input())

arr = [True for _ in range(104)]
prime = []

for i in range(2, 104):
    if arr[i]:
        prime.append(i)
        j = 2
        while i * j < 104:
            arr[i * j] = False
            j += 1

for i in range(1, len(prime)):
    num = prime[i - 1] * prime[i]
    if num > n:
        print(num)
        break