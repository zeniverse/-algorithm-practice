n = 626331
count = 0

while n != 1:
    count += 1

    if n % 2 == 0:
        n = n //2
    else:
        n = (n * 3) + 1

    if count > 500:
        print(-1)
        break

if n == 1:
    print(count)

