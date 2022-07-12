
numbers = [1,2,3,4,6,7,8,0]
numbers = set(numbers)
res = 0

for i in range(0, 10):
    if i not in numbers:
        res += i

print(res)