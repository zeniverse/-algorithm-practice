n = int(input())
arr = []
num = 1

while num <= 104:
    for i in range(2, num + 1):
        if num % i == 0:
            if num == i:
                arr.append(i)
                break
    num += 1

i = 0
while n >= arr[i] * arr[i + 1]:
    i += 1

print(arr[i] * arr[i + 1])