
brown = 8
yellow = 1

total = brown + yellow

for i in range(3, brown):
    if total % i == 0:
        j = total // i

        if (i - 2) * (j - 2) == yellow:
            print(sorted([i, j], reverse=True))
            break
