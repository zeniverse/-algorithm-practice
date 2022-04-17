arr = []

for _ in range(9):
    a = int(input())
    arr.append(a)

max_num = max(arr)

print(max_num)
print(arr.index(max_num) + 1)
