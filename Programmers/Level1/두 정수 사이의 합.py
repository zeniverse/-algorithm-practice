a = 5
b = 3

if a > b:
    a, b = b, a

print(sum([i for i in range(a, b + 1)]))