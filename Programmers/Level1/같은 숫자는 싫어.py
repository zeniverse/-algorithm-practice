arr = [1, 1, 3, 3, 0, 1, 1]
stack = []

for i in arr:
    if [i] != stack[-1:]:
        stack.append(i)

print(stack)