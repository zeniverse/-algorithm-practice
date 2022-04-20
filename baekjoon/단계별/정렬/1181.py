arr = []

for _ in range(int(input())):
    word = input()
    arr.append(word)


arr = sorted(list(set(arr)))
arr.sort(key=lambda x: len(x))

[print(i) for i in arr]