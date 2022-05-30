a = int(input())
b = int(input())

prime = []

for num in range(a, b + 1):
    if num > 1:
        check = True

        for j in range(2, num):
            if num % j == 0:
                check = False
                break

        if check:
            prime.append(num)

if prime:
    print(sum(prime))
    print(min(prime))
else:
    print(-1)