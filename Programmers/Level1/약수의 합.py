import math

n = 12

def get_divisor(num):
    data = set()

    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            data.add(i)
            data.add(num//i)

    return sum(data)

print(get_divisor(n))

        