arr = []

for _ in range(int(input())):
    age, name = input().split()
    age = int(age)
    arr.append((age, name))

arr.sort(key=lambda x:x[0])

for i in arr:
    print(i[0], i[1])