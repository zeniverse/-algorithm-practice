n = int(input())

c = n
count = 0

while True:

    a = int(c) % 10
    b = int(c) // 10

    c = (a * 10) + (a + b) % 10

    count += 1

    if c == n:
        break

print(count)