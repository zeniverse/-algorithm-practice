import math

left = 24
right = 27

res = 0


def get_divisor(n):
    data = set()

    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            data.add(i)
            data.add(n//i)

    return len(data)

for i in range(left, right + 1):
    count = get_divisor(i)

    if count % 2 == 0:
        res += i
    else:
        res -= i

print(res)