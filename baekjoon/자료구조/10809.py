s = input()
arr = [chr(i) for i in range(97, 123)]

for i in arr:
    print(s.find(i), end=" ")
