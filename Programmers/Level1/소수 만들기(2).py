from itertools import combinations

nums = [1, 2, 3, 4]

res = 0

for numbers in combinations(nums, 3):
    total = sum(numbers)

    for i in range(2, total):
        if total % i == 0:
            break
    else:
        res += 1

print(res)



