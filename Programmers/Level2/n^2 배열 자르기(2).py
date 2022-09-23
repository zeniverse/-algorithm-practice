
n = 4
left = 7
right = 14

arr = []

for i in range(left, right + 1):
    arr.append(max(i//n, i%n) + 1)

print(arr)